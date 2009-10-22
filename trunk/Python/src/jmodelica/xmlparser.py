# -*- coding: utf-8 -*-
"""Module containing XML parser and validator providing an XML object which 
can be used to extract information from the parsed XML file using XPath 
queries.
"""
#    Copyright (C) 2009 Modelon AB
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3 of the License.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from lxml import etree
import os.path
import numpy as N

int = N.int32
N.int = N.int32

def _parse_XML(filename, schemaname=''):
    
    """ 
    Parses and validates (optional) an XML file.
    
    Parses an XML file and returns an object representing the parsed XML.
    If the optional parameter schemaname is set the XML file is also validated
    against the XML Schema file provided before parsing. 
    
    Parameters:
        filename -- 
            Name of XML file to parse including absolute or relative path.
        schemaname --
            Name of XML Schema file including absolute or relative path.
        
    Exceptions:   
        XMLException -- 
            If the XML file can not be read or is not well-formed. If a schema 
            is present and if the schema file can not be read, is not 
            well-formed or if the validation fails. 
        
    Returns:    
        Reference to the ElementTree object containing the parsed XML.
        
    """
    
    try:
        xmldoc = etree.ElementTree(file=filename)
    except etree.XMLSyntaxError, detail:
        raise XMLException("The XML file: %s is not well-formed. %s" %(filename, detail))
    
    if schemaname:
        try:
            schemadoc = etree.ElementTree(file=schemaname)
        except etree.XMLSyntaxError, detail:
            raise XMLException("The XMLSchema: %s is not well-formed. %s" %(schemaname, detail))         
            
        schema = etree.XMLSchema(schemadoc)
        
        result = schema.validate(xmldoc)
        
        if not result:
            raise XMLException("The XML file: %s is not valid according to the XMLSchema: %s." %(filename, schemaname))
        
    return xmldoc

class XMLdoc:
    
    """ Base class representing a parsed XML file."""
    
    def __init__(self, filename, schemaname=''):
        """ 
        Create an XML document object representation and an XPath evaluator.
        
        Parse an XML document and create an XML document object 
        representation. Validate against XML schema before parsing if the 
        parameter schemaname is set. Instantiates an XPath evaluator object 
        for the parsed XML which can be used to evaluate XPath expressions on 
        the XML.
         
        """
        self._doc = _parse_XML(filename, schemaname)
        self._xpatheval = etree.XPathEvaluator(self._doc)

class XMLVariablesDoc(XMLdoc):    
    """ Class representing a parsed XML file containing model variable meta data. """
    
    def get_valueref(self, variablename):
        """
        Extract the ValueReference given a variable name.
        
        Parameters:
            variablename -- the name of the variable
            
        Returns:
            The ValueReference for the variable passed as argument.
        """
        ref = self._xpatheval("//ScalarVariable/ValueReference/text() [../../ScalarVariableName=\""+variablename+"\"]")
        if len(ref) > 0:
            return int(ref[0])
        else:
            return None
        
    def get_data_type(self, valueref):
        """ Get data type of variable. """
        type = self._xpatheval("//ScalarVariable/DataType/text()[../../ValueReference=\""+str(valueref)+"\"]")
        if len(type)>0:
            return str(type[0])
        return None

    def get_variable_names(self):
        """
        Extract the names of the variables in a model.

        Returns:
            Dict with ValueReference as key and name as value.
        """
        keys = self._xpatheval("//ScalarVariable/ValueReference/text() [../../AliasVariable=\"noAlias\"]")
        vals = self._xpatheval("//ScalarVariable/ScalarVariableName/text() [../../AliasVariable=\"noAlias\"]")       
        if len(keys)!=len(vals):
            raise Exception("Number of vals does not equal number of keys. \
                Number of vals are: "+str(len(vals))+" and number of keys are: "+str(len(keys)))
        valrefs=[]
        names=[]       
        for index, key in enumerate(keys):
            valrefs.append(int(key))
            names.append(str(vals[index]))
          
        return dict(zip(valrefs,names))

    def get_derivative_names(self):
        """
        Extract the names of the derivatives in a model.

        Returns:
            Dict with ValueReference as key and name as value.
        """
        keys = self._xpatheval("//ScalarVariable/ValueReference/text() [../../VariableCategory=\"derivative\"] \
            [../../AliasVariable=\"noAlias\"]")
        vals = self._xpatheval("//ScalarVariable/ScalarVariableName/text()[../../VariableCategory=\"derivative\"] \
            [../../AliasVariable=\"noAlias\"]")
        if len(keys)!=len(vals):
            raise Exception("Number of vals does not equal number of keys. \
                Number of vals are: "+str(len(vals))+" and number of keys are: "+str(len(keys)))
        valrefs=[]
        names=[]
        for index, key in enumerate(keys):
            valrefs.append(int(key))
            names.append(str(vals[index]))

        return dict(zip(valrefs,names))

    def get_differentiated_variable_names(self):
        """
        Extract the names of the differentiated variables in a model.

        Returns:
            Dict with ValueReference as key and name as value.
        """
        keys = self._xpatheval("//ScalarVariable/ValueReference/text() [../../VariableCategory=\"state\"] \
            [../../AliasVariable=\"noAlias\"]")
        vals = self._xpatheval("//ScalarVariable/ScalarVariableName/text()[../../VariableCategory=\"state\"] \
            [../../AliasVariable=\"noAlias\"]")
        if len(keys)!=len(vals):
            raise Exception("Number of vals does not equal number of keys. \
                Number of vals are: "+str(len(vals))+" and number of keys are: "+str(len(keys)))
        valrefs=[]
        names=[]
        for index, key in enumerate(keys):
            valrefs.append(int(key))
            names.append(str(vals[index]))

        return dict(zip(valrefs,names))

    def get_input_names(self):
        """
        Extract the names of the inputs in a model.

        Returns:
            Dict with ValueReference as key and name as value.
        """
        keys = self._xpatheval("//ScalarVariable/ValueReference/text() [../../Causality=\"input\"][../../VariableCategory=\"algebraic\"] \
            [../../AliasVariable=\"noAlias\"]")
        vals = self._xpatheval("//ScalarVariable/ScalarVariableName/text()[../../Causality=\"input\"][../../VariableCategory=\"algebraic\"] \
            [../../AliasVariable=\"noAlias\"]")
        if len(keys)!=len(vals):
            raise Exception("Number of vals does not equal number of keys. \
                Number of vals are: "+str(len(vals))+" and number of keys are: "+str(len(keys)))
        valrefs=[]
        names=[]
        for index, key in enumerate(keys):
            valrefs.append(int(key))
            names.append(str(vals[index]))
  
        return dict(zip(valrefs,names))

    def get_algebraic_variable_names(self):
        """
        Extract the names of the algebraic variables in a model.

        Returns:
            Dict with ValueReference as key and name as value.
        """
        keys = self._xpatheval("//ScalarVariable/ValueReference/text() [../../VariableCategory=\"algebraic\"][../../Causality!=\"input\"] \
            [../../AliasVariable=\"noAlias\"]")
        vals = self._xpatheval("//ScalarVariable/ScalarVariableName/text()[../../VariableCategory=\"algebraic\"][../../Causality!=\"input\"] \
            [../../AliasVariable=\"noAlias\"]")
        if len(keys)!=len(vals):
            raise Exception("Number of vals does not equal number of keys. \
                Number of vals are: "+str(len(vals))+" and number of keys are: "+str(len(keys)))
        valrefs=[]
        names=[]
        for index, key in enumerate(keys):
            valrefs.append(int(key))
            names.append(str(vals[index]))

        return dict(zip(valrefs,names))

    def get_p_opt_names(self):
        """ 
        Extract the names for all optimized independent parameters.
        
        Returns:
            Dict with ValueReference as key and name as value.
            
        """
        keys = self._xpatheval("//ScalarVariable/ValueReference/text()[../../VariableCategory=\"independentParameter\"] \
                               [../../Attributes/RealAttributes/Free=\"true\"] [../../AliasVariable=\"noAlias\"]")
        vals = self._xpatheval("//ScalarVariable/ScalarVariableName/text()[../../VariableCategory=\"independentParameter\"] \
                               [../../Attributes/RealAttributes/Free=\"true\"] [../../AliasVariable=\"noAlias\"]")
        if len(keys)!=len(vals):
            raise Exception("Number of vals does not equal number of keys. \
                Number of vals are: "+str(len(vals))+" and number of keys are: "+str(len(keys)))
        valrefs=[]
        names=[]
        for index, key in enumerate(keys):
            valrefs.append(int(key))
            names.append(str(vals[index]))

        return dict(zip(valrefs,names))

    def get_variable_descriptions(self):
        """
        Extract the descriptions of the variables in a model.

        Returns:
            Dict with ValueReference as key and description as value.
        """
        keys = self._xpatheval("//ScalarVariable/ValueReference/text() [../../Description] [../../AliasVariable=\"noAlias\"]")
        vals = self._xpatheval("//ScalarVariable/Description/text() [../../Description] [../../AliasVariable=\"noAlias\"]")
        if len(keys)!=len(vals):
            raise Exception("Number of vals does not equal number of keys. \
                Number of vals are: "+str(len(vals))+" and number of keys are: "+str(len(keys)))
        valrefs=[]
        descriptions=[]
        for index, key in enumerate(keys):
            valrefs.append(int(key))
            descriptions.append(str(vals[index]))

        return dict(zip(valrefs,descriptions))
    
    def _cast_values(self, keys, vals):
        valrefs=[]
        typed_values=[]
        for index, key in enumerate(keys):
            valrefs.append(int(key))
            type = self.get_data_type(int(key))
            if type == 'Real':
                typed_values.append(float(vals[index]))
            elif type == 'Integer':
                typed_values.append(int(vals[index]))
            elif type == 'Boolean':
                typed_values.append(vals[index]=="true")
            elif type == 'String':
                typed_values.append(str(vals[index]))
            else:
                pass
                # enumeration not supported yet
       
        return dict(zip(valrefs,typed_values))
    
    def get_start_attributes(self):
        """ 
        Extract ValueReference and Start attribute for all (non-alias) variables 
        in the XML document.
            
        Returns:
            Dict with ValueReference as key and Start attribute as value.
             
        """
        keys = self._xpatheval("//ScalarVariable/ValueReference/text() [../../AliasVariable=\"noAlias\"]")
        vals = self._xpatheval("//ScalarVariable/Attributes/*/Start/text() [../../../../AliasVariable=\"noAlias\"]")       
        if len(keys)!=len(vals):
            raise Exception("Number of vals does not equal number of keys. \
                Number of vals are: "+str(len(vals))+" and number of keys are: "+str(len(keys)))
#        keys = map(N.int,keys)
#        vals = map(N.float,vals)
        return self._cast_values(keys, vals)

    def get_dx_start_attributes(self):
        """ 
        Extract ValueReference and Start attribute for all derivatives in the 
        XML document.
            
        Returns:
            Dict with ValueReference as key and Start attribute as value.
             
        """
        keys = self._xpatheval("//ScalarVariable/ValueReference/text()[../../VariableCategory=\"derivative\"][../../Attributes/*/Start] \
            [../../AliasVariable=\"noAlias\"]")
        vals = self._xpatheval("//ScalarVariable/Attributes/*/Start/text()[../../../../VariableCategory=\"derivative\"] \
            [../../../../AliasVariable=\"noAlias\"]")       
        if len(keys)!=len(vals):
            raise Exception("Number of vals does not equal number of keys. \
                Number of vals are: "+str(len(vals))+" and number of keys are: "+str(len(keys)))
        return self._cast_values(keys, vals)

    def get_x_start_attributes(self):
        """ 
        Extract ValueReference and Start attribute for all differentiated 
        variables in the XML document.
            
        Returns:
            Dict with ValueReference as key and Start attribute as value.
             
        """
        keys = self._xpatheval("//ScalarVariable/ValueReference/text()[../../VariableCategory=\"state\"][../../Attributes/*/Start] \
            [../../AliasVariable=\"noAlias\"]")
        vals = self._xpatheval("//ScalarVariable/Attributes/*/Start/text()[../../../../VariableCategory=\"state\"] \
            [../../../../AliasVariable=\"noAlias\"]")       
        if len(keys)!=len(vals):
            raise Exception("Number of vals does not equal number of keys. \
                Number of vals are: "+str(len(vals))+" and number of keys are: "+str(len(keys)))
        return self._cast_values(keys, vals)

    def get_u_start_attributes(self):
        """ 
        Extract ValueReference and Start attribute for all inputs in the XML 
        document.
            
        Returns:
            Dict with ValueReference as key and Start attribute as value.
             
        """
        keys = self._xpatheval("//ScalarVariable/ValueReference/text()[../../Causality=\"input\"][../../VariableCategory=\"algebraic\"] \
            [../../Attributes/*/Start] [../../AliasVariable=\"noAlias\"]")
        vals = self._xpatheval("//ScalarVariable/Attributes/*/Start/text()[../../../../Causality=\"input\"] \
            [../../../../VariableCategory=\"algebraic\"] [../../../../AliasVariable=\"noAlias\"]")       
        if len(keys)!=len(vals):
            raise Exception("Number of vals does not equal number of keys. \
                Number of vals are: "+str(len(vals))+" and number of keys are: "+str(len(keys)))
        return self._cast_values(keys, vals)

    def get_w_start_attributes(self):
        """ 
        Extract ValueReference and Start attribute for all algebraic variables 
        in the XML document.
            
        Returns:
            Dict with ValueReference as key and Start attribute as value.
             
        """
        keys = self._xpatheval("//ScalarVariable/ValueReference/text()[../../VariableCategory=\"algebraic\"][../../Causality!=\"input\"] \
            [../../AliasVariable=\"noAlias\"]")
        vals = self._xpatheval("//ScalarVariable/Attributes/*/Start/text()[../../../../VariableCategory=\"algebraic\"] \
            [../../../../Causality!=\"input\"] [../../../../AliasVariable=\"noAlias\"]")       
        if len(keys)!=len(vals):
            raise Exception("Number of vals does not equal number of keys. \
                Number of vals are: "+str(len(vals))+" and number of keys are: "+str(len(keys)))
        return self._cast_values(keys, vals)
    
    def get_p_opt_variable_refs(self):
        """ 
        Extract ValueReference for all optimized independent parameters.
        
        Returns:
            List of ValueReferences for all optimized independent parameters.
            
        """
        refs = self._xpatheval("//ScalarVariable/ValueReference/text()[../../VariableCategory=\"independentParameter\"] \
                               [../../Attributes/RealAttributes/Free=\"true\"] [../../AliasVariable=\"noAlias\"]")
        valrefs=[]
        for ref in refs:
            valrefs.append(int(ref))
        return valrefs
    
    def get_w_initial_guess_values(self):
        """ 
        Extract ValueReference and InitialGuess values for all algebraic 
        variables.
        
        Returns:
            Dict with ValueReference as key and InitialGuess as value.
        
        """
        keys = self._xpatheval("//ScalarVariable/ValueReference/text()[../../VariableCategory=\"algebraic\"] \
            [../../Causality!=\"input\"] [../../AliasVariable=\"noAlias\"]")
        vals = self._xpatheval("//ScalarVariable/Attributes/RealAttributes/InitialGuess/text()[../../../../VariableCategory=\"algebraic\"] \
            [../../../../Causality!=\"input\"] [../../../../AliasVariable=\"noAlias\"]")
        if len(keys)!=len(vals):
            raise Exception("Number of vals does not equal number of keys. \
                Number of vals are: "+str(len(vals))+" and number of keys are: "+str(len(keys)))
        return self._cast_values(keys, vals)
    
    def get_u_initial_guess_values(self):
        """ 
        Extract ValueReference and InitialGuess values for all input 
        variables.
        
        Returns:
            Dict with ValueReference as key and InitialGuess as value.
            
        """
        keys = self._xpatheval("//ScalarVariable/ValueReference/text()[../../Causality=\"input\"][../../VariableCategory=\"algebraic\"] \
            [../../AliasVariable=\"noAlias\"]")
        vals = self._xpatheval("//ScalarVariable/Attributes/RealAttributes/InitialGuess/text()[../../../../Causality=\"input\"] \
            [../../../../VariableCategory=\"algebraic\"] [../../../../AliasVariable=\"noAlias\"]")
        if len(keys)!=len(vals):
            raise Exception("Number of vals does not equal number of keys. \
                Number of vals are: "+str(len(vals))+" and number of keys are: "+str(len(keys)))
        return self._cast_values(keys, vals)
    
    def get_dx_initial_guess_values(self):
        """ 
        Extract ValueReference and InitialGuess values for all derivative 
        variables.
        
        Returns:
            Dict with ValueReference as key and InitialGuess as value.
            
        """
        keys = self._xpatheval("//ScalarVariable/ValueReference/text()[../../VariableCategory=\"derivative\"] \
            [../../AliasVariable=\"noAlias\"]")
        vals = self._xpatheval("//ScalarVariable/Attributes/RealAttributes/InitialGuess/text()[../../../../VariableCategory=\"derivative\"] \
            [../../../../AliasVariable=\"noAlias\"]")
        if len(keys)!=len(vals):
            raise Exception("Number of vals does not equal number of keys. \
                Number of vals are: "+str(len(vals))+" and number of keys are: "+str(len(keys)))
        return self._cast_values(keys, vals)
    
    def get_x_initial_guess_values(self):
        """ 
        Extract ValueReference and InitialGuess values for all differentiated 
        variables.
        
        Returns:
            Dict with ValueReference as key and InitialGuess as value.
            
        """
        keys = self._xpatheval("//ScalarVariable/ValueReference/text()[../../VariableCategory=\"state\"] \
            [../../AliasVariable=\"noAlias\"]")
        vals = self._xpatheval("//ScalarVariable/Attributes/RealAttributes/InitialGuess/text()[../../../../VariableCategory=\"state\"] \
            [../../../../AliasVariable=\"noAlias\"]")
        if len(keys)!=len(vals):
            raise Exception("Number of vals does not equal number of keys. \
                Number of vals are: "+str(len(vals))+" and number of keys are: "+str(len(keys)))        
        return self._cast_values(keys, vals)
    
    def get_p_opt_initial_guess_values(self):
        """ 
        Extract ValueReference and InitialGuess values for all optimized 
        independent parameters.
        
        Returns:
            Dict with ValueReference as key and InitialGuess as value.
        
        """
        keys = self._xpatheval("//ScalarVariable/ValueReference/text()[../../VariableCategory=\"independentParameter\"] \
                                [../../Attributes/RealAttributes/Free=\"true\"] [../../AliasVariable=\"noAlias\"]")
        vals = self._xpatheval("//ScalarVariable/Attributes/RealAttributes/InitialGuess/text()[../../../../VariableCategory=\"independentParameter\"] \
                                [../../../../Attributes/RealAttributes/Free=\"true\"] [../../../../AliasVariable=\"noAlias\"]")
        if len(keys)!=len(vals):
            raise Exception("Number of vals does not equal number of keys. \
                Number of vals are: "+str(len(vals))+" and number of keys are: "+str(len(keys)))
        return self._cast_values(keys, vals)

    def get_w_lb_values(self):
        """ 
        Extract ValueReference and lower bound values for all algebraic 
        variables.
        
        Returns:
            Dict with ValueReference as key and lower bound as value.
        
        """
        keys = self._xpatheval("//ScalarVariable/ValueReference/text()[../../VariableCategory=\"algebraic\"][../../Causality!=\"input\"] \
            [../../Attributes/*/Min] [../../AliasVariable=\"noAlias\"]")
        vals = self._xpatheval("//ScalarVariable/Attributes/RealAttributes/Min/text()[../../../../VariableCategory=\"algebraic\"] \
            [../../../../Causality!=\"input\"] [../../../../AliasVariable=\"noAlias\"]")
        if len(keys)!=len(vals):
            raise Exception("Number of vals does not equal number of keys. \
                Number of vals are: "+str(len(vals))+" and number of keys are: "+str(len(keys)))
        return self._cast_values(keys, vals)
    
    def get_u_lb_values(self):
        """ 
        Extract ValueReference and lower bound values for all input 
        variables.
        
        Returns:
            Dict with ValueReference as key and lower bound as value.
            
        """
        keys = self._xpatheval("//ScalarVariable/ValueReference/text()[../../Causality=\"input\"][../../VariableCategory=\"algebraic\"] \
            [../../Attributes/*/Min] [../../AliasVariable=\"noAlias\"]")
        vals = self._xpatheval("//ScalarVariable/Attributes/RealAttributes/Min/text()[../../../../Causality=\"input\"] \
            [../../../../VariableCategory=\"algebraic\"] [../../../../AliasVariable=\"noAlias\"]")
        if len(keys)!=len(vals):
            raise Exception("Number of vals does not equal number of keys. \
                Number of vals are: "+str(len(vals))+" and number of keys are: "+str(len(keys)))            
        return self._cast_values(keys, vals)
    
    def get_dx_lb_values(self):
        """ 
        Extract ValueReference and lower bound values for all derivative 
        variables.
        
        Returns:
            Dict with ValueReference as key and lower bound as value.
            
        """
        keys = self._xpatheval("//ScalarVariable/ValueReference/text()[../../VariableCategory=\"derivative\"] \
            [../../Attributes/*/Min] [../../AliasVariable=\"noAlias\"]")
        vals = self._xpatheval("//ScalarVariable/Attributes/RealAttributes/Min/text()[../../../../VariableCategory=\"derivative\"] \
            [../../../../AliasVariable=\"noAlias\"]")
        if len(keys)!=len(vals):
            raise Exception("Number of vals does not equal number of keys. \
                Number of vals are: "+str(len(vals))+" and number of keys are: "+str(len(keys)))        
        return self._cast_values(keys, vals)
    
    def get_x_lb_values(self):
        """ 
        Extract ValueReference and lower bound values for all differentiated 
        variables.
        
        Returns:
            Dict with ValueReference as key and lower bound as value.
            
        """
        keys = self._xpatheval("//ScalarVariable/ValueReference/text()[../../VariableCategory=\"state\"] [../../Attributes/*/Min] \
            [../../AliasVariable=\"noAlias\"]")
        vals = self._xpatheval("//ScalarVariable/Attributes/RealAttributes/Min/text()[../../../../VariableCategory=\"state\"] \
            [../../../../AliasVariable=\"noAlias\"]")
        if len(keys)!=len(vals):
            raise Exception("Number of vals does not equal number of keys. \
                Number of vals are: "+str(len(vals))+" and number of keys are: "+str(len(keys)))
        return self._cast_values(keys, vals)
    
    def get_p_opt_lb_values(self):
        """ 
        Extract ValueReference and lower bound values for all optimized 
        independent parameters.
        
        Returns:
            Dict with ValueReference as key and lower bound as value.
            
        """
        keys = self._xpatheval("//ScalarVariable/ValueReference/text()[../../VariableCategory=\"independentParameter\"] \
                               [../../Attributes/RealAttributes/Free=\"true\"] [../../Attributes/*/Min] [../../AliasVariable=\"noAlias\"]")
        vals = self._xpatheval("//ScalarVariable/Attributes/RealAttributes/Min/text()[../../../../VariableCategory=\"independentParameter\"] \
                               [../../../../Attributes/RealAttributes/Free=\"true\"] [../../../../AliasVariable=\"noAlias\"]")
        if len(keys)!=len(vals):
            raise Exception("Number of vals does not equal number of keys. \
                Number of vals are: "+str(len(vals))+" and number of keys are: "+str(len(keys)))
        return self._cast_values(keys, vals)

    def get_w_ub_values(self):
        """ 
        Extract ValueReference and upper bound values for all algebraic 
        variables.
        
        Returns:
            Dict with ValueReference as key and upper bound as value.
            
        """
        keys = self._xpatheval("//ScalarVariable/ValueReference/text()[../../VariableCategory=\"algebraic\"][../../Causality!=\"input\"] \
            [../../Attributes/*/Max] [../../AliasVariable=\"noAlias\"]")
        vals = self._xpatheval("//ScalarVariable/Attributes/RealAttributes/Max/text()[../../../../VariableCategory=\"algebraic\"] \
            [../../../../Causality!=\"input\"] [../../../../AliasVariable=\"noAlias\"]")
        if len(keys)!=len(vals):
            raise Exception("Number of vals does not equal number of keys. \
                Number of vals are: "+str(len(vals))+" and number of keys are: "+str(len(keys)))           
        return self._cast_values(keys, vals)

    def get_u_ub_values(self):
        """ 
        Extract ValueReference and upper bound values for all input variables.
        
        Returns:
            Dict with ValueReference as key and upper bound as value.
            
        """
        keys = self._xpatheval("//ScalarVariable/ValueReference/text()[../../Causality=\"input\"][../../VariableCategory=\"algebraic\"] \
            [../../Attributes/*/Max][../../AliasVariable=\"noAlias\"]")
        vals = self._xpatheval("//ScalarVariable/Attributes/RealAttributes/Max/text()[../../../../Causality=\"input\"] \
            [../../../../VariableCategory=\"algebraic\"] [../../../../AliasVariable=\"noAlias\"]")    
        if len(keys)!=len(vals):
            raise Exception("Number of vals does not equal number of keys. \
                Number of vals are: "+str(len(vals))+" and number of keys are: "+str(len(keys)))
        return self._cast_values(keys, vals)
    
    def get_dx_ub_values(self):
        """ 
        Extract ValueReference and upper bound values for all derivative 
        variables.
        
        Returns:
            Dict with ValueReference as key and upper bound as value.
            
        """
        keys = self._xpatheval("//ScalarVariable/ValueReference/text()[../../VariableCategory=\"derivative\"] [../../Attributes/*/Max] \
            [../../AliasVariable=\"noAlias\"]")
        vals = self._xpatheval("//ScalarVariable/Attributes/RealAttributes/Max/text()[../../../../VariableCategory=\"derivative\"] \
            [../../../../AliasVariable=\"noAlias\"]")
        if len(keys)!=len(vals):
            raise Exception("Number of vals does not equal number of keys. \
                Number of vals are: "+str(len(vals))+" and number of keys are: "+str(len(keys)))
        return self._cast_values(keys, vals)
    
    def get_x_ub_values(self):
        """ 
        Extract ValueReference and upper bound values for all differentiated 
        variables.
        
        Returns:
            Dict with ValueReference as key and upper bound as value.
            
        """
        keys = self._xpatheval("//ScalarVariable/ValueReference/text()[../../VariableCategory=\"state\"] [../../Attributes/*/Max] \
            [../../AliasVariable=\"noAlias\"]")
        vals = self._xpatheval("//ScalarVariable/Attributes/RealAttributes/Max/text()[../../../../VariableCategory=\"state\"] \
            [../../../../AliasVariable=\"noAlias\"]")
        if len(keys)!=len(vals):
            raise Exception("Number of vals does not equal number of keys. \
                Number of vals are: "+str(len(vals))+" and number of keys are: "+str(len(keys)))        
        return self._cast_values(keys, vals)
    
    def get_p_opt_ub_values(self):
        """ 
        Extract ValueReference and upper bound values for all optimized 
        independent parameters.
        
        Returns:
            Dict with ValueReference as key and upper bound as value.
            
        """
        keys = self._xpatheval("//ScalarVariable/ValueReference/text()[../../VariableCategory=\"independentParameter\"] \
                               [../../Attributes/RealAttributes/Free=\"true\"] [../../Attributes/*/Max] [../../AliasVariable=\"noAlias\"]")
        vals = self._xpatheval("//ScalarVariable/Attributes/RealAttributes/Max/text()[../../../../VariableCategory=\"independentParameter\"] \
                               [../../../../Attributes/RealAttributes/Free=\"true\"] [../../../../AliasVariable=\"noAlias\"]")        
        if len(keys)!=len(vals):
            raise Exception("Number of vals does not equal number of keys. \
                Number of vals are: "+str(len(vals))+" and number of keys are: "+str(len(keys)))
        return self._cast_values(keys, vals)
    

    def get_w_lin_values(self):
        """ 
        Extract ValueReference and boolean value describing if variable 
        appears linearly in all equations and constraints for all algebraic 
        variables.
        
        Returns:
            Dict with ValueReference as key and boolean isLinear as value.
            
        """
        keys = self._xpatheval("//ScalarVariable/ValueReference/text()[../../VariableCategory=\"algebraic\"][../../Causality!=\"input\"] \
            [../../IsLinear] [../../AliasVariable=\"noAlias\"]")
        vals = self._xpatheval("//ScalarVariable/IsLinear/text()[../../VariableCategory=\"algebraic\"][../../Causality!=\"input\"] \
            [../../AliasVariable=\"noAlias\"]")
        if len(keys)!=len(vals):
            raise Exception("Number of vals does not equal number of keys. \
                Number of vals are: "+str(len(vals))+" and number of keys are: "+str(len(keys)))
        valrefs = []
        islinears = []
        for index, key in enumerate(keys):
            valrefs.append(int(key))
            islinears.append(vals[index]=="true") 
        return dict(zip(valrefs, islinears))

    def get_u_lin_values(self):
        """ 
        Extract ValueReference and boolean value describing if variable 
        appears linearly in all equations and constraints for all input 
        variables.
        
        Returns:
            Dict with ValueReference as key and boolean isLinear as value.

        """
        keys = self._xpatheval("//ScalarVariable/ValueReference/text()[../../Causality=\"input\"][../../VariableCategory=\"algebraic\"] \
            [../../IsLinear] [../../AliasVariable=\"noAlias\"]")
        vals = self._xpatheval("//ScalarVariable/IsLinear/text()[../../Causality=\"input\"][../../VariableCategory=\"algebraic\"] \
            [../../AliasVariable=\"noAlias\"]")            
        if len(keys)!=len(vals):
            raise Exception("Number of vals does not equal number of keys. \
                Number of vals are: "+str(len(vals))+" and number of keys are: "+str(len(keys)))
        valrefs = []
        islinears = []
        for index, key in enumerate(keys):
            valrefs.append(int(key))
            islinears.append(vals[index]=="true")    
        return dict(zip(valrefs, islinears))
    
    def get_dx_lin_values(self):
        """ 
        Extract ValueReference and boolean value describing if variable 
        appears linearly in all equations and constraints for all derivative 
        variables.
        
        Returns:
            Dict with ValueReference as key and boolean isLinear as value.

        """
        keys = self._xpatheval("//ScalarVariable/ValueReference/text()[../../VariableCategory=\"derivative\"][../../IsLinear] \
            [../../AliasVariable=\"noAlias\"]")
        vals = self._xpatheval("//ScalarVariable/IsLinear/text()[../../VariableCategory=\"derivative\"] \
            [../../AliasVariable=\"noAlias\"]")        
        if len(keys)!=len(vals):
            raise Exception("Number of vals does not equal number of keys. \
                Number of vals are: "+str(len(vals))+" and number of keys are: "+str(len(keys)))
        valrefs = []
        islinears = []
        for index, key in enumerate(keys):
            valrefs.append(int(key))
            islinears.append(vals[index]=="true")
        return dict(zip(valrefs, islinears))
    
    def get_x_lin_values(self):
        """ 
        Extract ValueReference and boolean value describing if variable 
        appears linearly in all equations and constraints for all 
        differentiated variables.
        
        Returns:
            Dict with ValueReference as key and boolean isLinear as value.

        """
        keys = self._xpatheval("//ScalarVariable/ValueReference/text()[../../VariableCategory=\"state\"][../../IsLinear] \
            [../../AliasVariable=\"noAlias\"]")
        vals = self._xpatheval("//ScalarVariable/IsLinear/text()[../../VariableCategory=\"state\"] [../../AliasVariable=\"noAlias\"]")        
        if len(keys)!=len(vals):
            raise Exception("Number of vals does not equal number of keys. \
                Number of vals are: "+str(len(vals))+" and number of keys are: "+str(len(keys)))
        valrefs = []
        islinears = []
        for index, key in enumerate(keys):
            valrefs.append(int(key))
            islinears.append(vals[index]=="true") 
        return dict(zip(valrefs, islinears))
    
    def get_p_opt_lin_values(self):
        """ 
        Extract ValueReference and boolean value describing if variable 
        appears linearly in all equations and constraints for all optimized 
        independent parameters.
        
        Returns:
            Dict with ValueReference as key and boolean isLinear as value.

        """
        keys = self._xpatheval("//ScalarVariable/ValueReference/text()[../../VariableCategory=\"independentParameter\"] \
                               [../../Attributes/RealAttributes/Free=\"true\"][../../IsLinear] [../../AliasVariable=\"noAlias\"]")
        vals = self._xpatheval("//ScalarVariable/IsLinear/text()[../../VariableCategory=\"independentParameter\"] \
                               [../../Attributes/RealAttributes/Free=\"true\"] [../../AliasVariable=\"noAlias\"]")                
        if len(keys)!=len(vals):
            raise Exception("Number of vals does not equal number of keys. \
                Number of vals are: "+str(len(vals))+" and number of keys are: "+str(len(keys)))
        valrefs = []
        islinears = []
        for index, key in enumerate(keys):
            valrefs.append(int(key))
            islinears.append(vals[index]=="true")    
        return dict(zip(valrefs, islinears))

    def get_w_lin_tp_values(self):
        """ 
        Extract ValueReference and linear timed variables for all algebraic 
        variables.
        
        Returns:
            Dict with ValueReference as key and boolean isLinear as value.

        """
        keys = self._xpatheval("//ScalarVariable/ValueReference/text()[../../VariableCategory=\"algebraic\"][../../Causality!=\"input\"] \
            [../../IsLinearTimedVariables] [../../AliasVariable=\"noAlias\"]")
        vals = []
        for key in keys:
            tp = self._xpatheval("//ScalarVariable/IsLinearTimedVariables/TimePoint/@isLinear[../../../VariableCategory=\"algebraic\"] \
                [../../../Causality!=\"input\"] [../../../ValueReference="+key+"] [../../../AliasVariable=\"noAlias\"]")
            vals.append(tp)        
        if len(keys)!=len(vals):
            raise Exception("Number of vals does not equal number of keys. \
                Number of vals are: "+str(len(vals))+" and number of keys are: "+str(len(keys)))
        valrefs = []
        timepoints_islinear = []
        
        for index, key in enumerate(keys):
            valrefs.append(int(key))
            # get list of timepoints for each valueref
            tps = vals[index]
            casted_tps = []
            for tp in tps:
                casted_tps.append(tp == "true")    
            timepoints_islinear.append(casted_tps)             
        return dict(zip(valrefs, timepoints_islinear))

    def get_u_lin_tp_values(self):
        """ 
        Extract ValueReference and linear timed variables for all input 
        variables.
        
        Returns:
            Dict with ValueReference as key and list of linear time variables 
            as value. 
        
        """
        keys = self._xpatheval("//ScalarVariable/ValueReference/text()[../../Causality=\"input\"][../../VariableCategory=\"algebraic\"] \
            [../../IsLinearTimedVariables] [../../AliasVariable=\"noAlias\"]")
        vals = []
        for key in keys:
            tp = self._xpatheval("//ScalarVariable/IsLinearTimedVariables/TimePoint/@isLinear[../../../Causality=\"input\"] \
                [../../../VariableCategory=\"algebraic\"] [../../../ValueReference="+key+"] [../../../AliasVariable=\"noAlias\"]")
            vals.append(tp)
        if len(keys)!=len(vals):
            raise Exception("Number of vals does not equal number of keys. \
                Number of vals are: "+str(len(vals))+" and number of keys are: "+str(len(keys)))
        valrefs = []
        timepoints_islinear = []
        
        for index, key in enumerate(keys):
            valrefs.append(int(key))
            # get list of timepoints for each valueref
            tps = vals[index]
            casted_tps = []
            for tp in tps:
                casted_tps.append(tp == "true")
            timepoints_islinear.append(casted_tps)             
        return dict(zip(valrefs, timepoints_islinear))
    
    def get_dx_lin_tp_values(self):
        """ 
        Extract ValueReference and linear timed variables for all derivative 
        variables.

        Returns:
            Dict with ValueReference as key and list of linear time variables 
            as value. 
        
        """
        keys = self._xpatheval("//ScalarVariable/ValueReference/text()[../../VariableCategory=\"derivative\"] \
            [../../IsLinearTimedVariables] [../../AliasVariable=\"noAlias\"]")
        vals = []
        for key in keys:
            tp = self._xpatheval("//ScalarVariable/IsLinearTimedVariables/TimePoint/@isLinear[../../../VariableCategory=\"derivative\"] \
                [../../../ValueReference="+key+"] [../../../AliasVariable=\"noAlias\"]")
            vals.append(tp)        
        if len(keys)!=len(vals):
            raise Exception("Number of vals does not equal number of keys. \
                Number of vals are: "+str(len(vals))+" and number of keys are: "+str(len(keys)))
        valrefs = []
        timepoints_islinear = []
        
        for index, key in enumerate(keys):
            valrefs.append(int(key))
            # get list of timepoints for each valueref
            tps = vals[index]
            casted_tps = []
            for tp in tps:
                casted_tps.append(tp == "true")
            timepoints_islinear.append(casted_tps)             
        return dict(zip(valrefs, timepoints_islinear))
    
    def get_x_lin_tp_values(self):
        """ 
        Extract ValueReference and linear timed variables for all 
        differentiated variables.

        Returns:
            Dict with ValueReference as key and list of linear time variables 
            as value. 
        
        """
        keys = self._xpatheval("//ScalarVariable/ValueReference/text()[../../VariableCategory=\"state\"][../../IsLinearTimedVariables] \
            [../../AliasVariable=\"noAlias\"]")
        vals = []        
        for key in keys:
            tp = self._xpatheval("//ScalarVariable/IsLinearTimedVariables/TimePoint/@isLinear[../../../VariableCategory=\"state\"] \
                [../../../ValueReference="+key+"] [../../../AliasVariable=\"noAlias\"]")
            vals.append(tp)
        if len(keys)!=len(vals):
            raise Exception("Number of vals does not equal number of keys. \
                Number of vals are: "+str(len(vals))+" and number of keys are: "+str(len(keys)))
        valrefs = []
        timepoints_islinear = []
        
        for index, key in enumerate(keys):
            valrefs.append(int(key))
            # get list of timepoints for each valueref
            tps = vals[index]
            casted_tps = []
            for tp in tps:
                casted_tps.append(tp == "true")
            timepoints_islinear.append(casted_tps)             
        return dict(zip(valrefs, timepoints_islinear))       
            
class XMLValuesDoc(XMLdoc):
    
    """ 
    Class representing a parsed XML file containing values for all 
    independent parameters. 
    
    """
                
    def get_iparam_values(self):
        """ 
        Extract ValueReference and value for all independent parameters in the 
        XML document.
        
        Returns:   
            Dict with ValueReference as key and parameter as value.
            
        """
        keys = self._xpatheval("//ValueReference/text()")
        vals = self._xpatheval("//Value/text()")
        if len(keys)!=len(vals):
            raise Exception("Number of vals does not equal number of keys. \
                Number of vals are: "+str(len(vals))+" and number of keys are: "+str(len(keys)))
        valrefs=[]
        iparam_values=[]
        for index, key in enumerate(keys):
            valrefs.append(int(key))
            type = self.get_parameter_type(int(key))
            if type == 'RealParameter':
                iparam_values.append(float(vals[index]))
            elif type == 'IntegerParameter':
                iparam_values.append(int(vals[index]))
            elif type == 'BooleanParameter':
                iparam_values.append(vals[index]=="true")
            elif type == 'StringParameter':
                iparam_values.append(str(vals[index]))
            else:
                pass
                # enumeration not supported yet
        return dict(zip(valrefs, iparam_values))
    
    def get_parameter_type(self, valref):
        type = self._xpatheval("//IndependentParameters/node()[ValueReference=\""+str(valref)+"\"]")
        if len(type) > 0:
            return type[0].tag
        return None
        
class XMLProblVariablesDoc(XMLdoc):
    
    """ 
    Class representing a parsed XML file containing Optimica problem 
    specification meta data. 
    
    """
    
    def get_starttime(self):
        """ Extract the interval start time. """
        time = self._xpatheval("//IntervalStartTime/Value/text()")
        if len(time) > 0:
            return float(time[0])
        return None

    def get_starttime_free(self):
        """ Extract the start time free attribute value. """
        free = self._xpatheval("//IntervalStartTime/Free/text()")
        if len(free) > 0:
            return (free[0]=="true")
        return None
    
    def get_finaltime(self):
        """ Extract the interval final time. """
        time = self._xpatheval("//IntervalFinalTime/Value/text()")
        if len(time) > 0:
            return float(time[0])
        return None

    def get_finaltime_free(self):
        """ Extract the final time free attribute value. """
        free = self._xpatheval("//IntervalFinalTime/Free/text()")
        if len(free) > 0:
            return (free[0]=="true")
        return None

    def get_timepoints(self):
        """ Extract all time points. """
        vals = self._xpatheval("//TimePoints/Value/text()")
        timepoints = []
        for tp in vals:
            timepoints.append(float(tp))
        return timepoints
     
class XMLException(Exception):
    
    """ Class for all XML related errors that can occur in this module. """
    
    pass
