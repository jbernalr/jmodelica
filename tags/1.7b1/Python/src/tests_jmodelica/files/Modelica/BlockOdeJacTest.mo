model BlockOdeJacTest
  output Real x_1(start=0.951858508368);
  output Real x_2(start=2.17691690118);
  output Real x_3(start=1.47982066619);
  output Real x_4(start=2.41568015438);
  output Real w_ode_1_1;
  Real w_ode_1_2;
  Real w_ode_1_3;
  output Real w_ode_2_1;
  Real w_ode_2_2;
  Real w_ode_2_3;
  output Real w_ode_3_1;
  Real w_ode_3_2;
  Real w_ode_3_3;
  output Real w_ode_4_1;
  Real w_ode_4_2;
  Real w_ode_4_3;
  output Real w_output_1_1;
  output Real w_output_1_2;
  output Real w_output_1_3;
  output Real w_output_2_1;
  output Real w_output_2_2;
  output Real w_output_2_3;
  output Real w_output_3_1;
  output Real w_output_3_2;
  output Real w_output_3_3;
  Real w_other_1_1;
  Real w_other_1_2;
  Real w_other_1_3;
  Real w_other_2_1;
  Real w_other_2_2;
  Real w_other_2_3;
  Real w_other_3_1;
  Real w_other_3_2;
  Real w_other_3_3;
  input Real ur_1;
  input Real ur_2;
  input Real ur_3;
  output Integer io1 = 1;
  output Boolean bo1 = true;
equation
w_ode_1_1*10 + 0.251440608216*w_ode_1_1 + 0.1*sin(w_ode_1_1)  + 0.674938164193*w_ode_1_2 + 0.1*sin(w_ode_1_2)  + 0.991289671021*(w_ode_1_3*w_ode_1_3*w_ode_1_3 + w_ode_1_3) + 0.26972131657*x_4 - 0.482503712403*x_2 + 0.516460492574*(x_3*x_3*x_3 + x_3) + -0.937976497061*x_1 + -0.210073191999*ur_2 + 0.871173443409*ur_3 + -0.728062279599*ur_3 + 0.1*sin(ur_3)  - -0.127676266745*(ur_3*ur_3*ur_3 + ur_3) + 0.0144859676581*(ur_3*ur_3*ur_3 + ur_3) = 0;
w_ode_1_2*10 + -0.29817902246*(w_ode_1_1*w_ode_1_1*w_ode_1_1 + w_ode_1_1) - 0.808403541696*w_ode_1_2 - 0.712801132794*w_ode_1_3 + 0.809391969024*(x_3*x_3*x_3 + x_3) - -0.577750032649*x_1 - -0.430085076028*x_4 + 0.1*sin(x_4)  - 0.979612029843*x_4 + 0.1*sin(x_4)  + 0.745534049256*ur_3 + 0.1*sin(ur_3)  - -0.910119513008*ur_2 + 0.761810614495*ur_1 - 0.997017890752*ur_1 + 0.1*sin(ur_1)  + 0.199525617593*ur_3 + 0.1*sin(ur_3)  = 0;
w_ode_1_3*10 + -0.605230287143*(w_ode_1_1*w_ode_1_1*w_ode_1_1 + w_ode_1_1) - -0.687602017973*w_ode_1_2 + 0.1*sin(w_ode_1_2)  - -0.372338960168*w_ode_1_3 + 0.287777436775*(x_4*x_4*x_4 + x_4) - 0.240252270891*x_2 - -0.137616893138*x_2 + -0.397826277652*x_3 + -0.959894219391*(ur_2*ur_2*ur_2 + ur_2) - -0.879838978745*(ur_2*ur_2*ur_2 + ur_2) + 0.358562796076*(ur_1*ur_1*ur_1 + ur_1) - 0.476068578504*ur_2 + 0.1*sin(ur_2)  + 0.352040618975*ur_2 = 0;

der(x_1) = -0.497755443633*(w_ode_1_1*w_ode_1_1*w_ode_1_1 + w_ode_1_1) - -0.359949228504*(w_ode_1_2*w_ode_1_2*w_ode_1_2 + w_ode_1_2) + -0.261692049446*(w_ode_1_3*w_ode_1_3*w_ode_1_3 + w_ode_1_3) + 0.138516004141*x_2 + -0.554924314414*x_2 + -0.625211318164*(x_4*x_4*x_4 + x_4) - -0.796316614736*x_1 + 0.1*sin(x_1)  + -0.32657952991*(ur_2*ur_2*ur_2 + ur_2) - -0.0977956314296*ur_3 + 0.1*sin(ur_3)  + 0.0592552566168*ur_2 + 0.1*sin(ur_2)  - 0.676952758056*ur_3 + 0.1*sin(ur_3)  + 0.614452836334*(ur_1*ur_1*ur_1 + ur_1);

w_ode_2_1*10 + 0.61251568227*(w_ode_2_1*w_ode_2_1*w_ode_2_1 + w_ode_2_1) + -0.416114218259*w_ode_2_2 + -0.307291438666*(w_ode_2_3*w_ode_2_3*w_ode_2_3 + w_ode_2_3) + -0.990676410834*x_2 - 0.973827310058*(x_2*x_2*x_2 + x_2) - 0.854754428823*x_4 + 0.1*sin(x_4)  - 0.673397358557*(x_1*x_1*x_1 + x_1) + 0.177355438038*ur_2 + 0.1*sin(ur_2)  - -0.909846379829*ur_1 - 0.847709599114*ur_2 - 0.153906808039*ur_1 + 0.1*sin(ur_1)  - -0.656356818927*ur_1 + 0.1*sin(ur_1)  = 0;
w_ode_2_2*10 + 0.32579220861*(w_ode_2_1*w_ode_2_1*w_ode_2_1 + w_ode_2_1) + 0.878084926502*(w_ode_2_2*w_ode_2_2*w_ode_2_2 + w_ode_2_2) + -0.495050311506*w_ode_2_3 + 0.0692740811056*x_2 + 0.583343837764*x_4 - 0.646997525107*x_2 + 0.1*sin(x_2)  - 0.725109136109*x_1 + 0.1*sin(x_1)  + 0.552995321446*ur_1 + 0.1*sin(ur_1)  + -0.746273427513*ur_1 + 0.1*sin(ur_1)  + 0.949385062352*ur_2 + 0.00424001350986*ur_2 + 0.1*sin(ur_2)  + -0.29742088339*(ur_2*ur_2*ur_2 + ur_2) = 0;
w_ode_2_3*10 + 0.173226241829*(w_ode_2_1*w_ode_2_1*w_ode_2_1 + w_ode_2_1) + -0.342447393705*w_ode_2_2 + 0.1*sin(w_ode_2_2)  - 0.432085644052*(w_ode_2_3*w_ode_2_3*w_ode_2_3 + w_ode_2_3) + 0.56524366947*(x_1*x_1*x_1 + x_1) - 0.24585302005*(x_1*x_1*x_1 + x_1) + -0.00769679605896*x_2 + 0.388246423279*(x_3*x_3*x_3 + x_3) + -0.148289887155*ur_1 - -0.251528606283*ur_2 - -0.475640548446*(ur_3*ur_3*ur_3 + ur_3) + 0.62644341188*(ur_1*ur_1*ur_1 + ur_1) - 0.584938770181*ur_2 = 0;

der(x_2) = 0.467470352626*(w_ode_2_1*w_ode_2_1*w_ode_2_1 + w_ode_2_1) + 0.175517539927*w_ode_2_2 + 0.1*sin(w_ode_2_2)  + 0.548608040641*w_ode_2_3 + 0.1*sin(w_ode_2_3)  + -0.81640224808*w_ode_1_1 + 0.1*sin(w_ode_1_1)  - -0.641692790099*w_ode_1_2 + 0.1*sin(w_ode_1_2)  - -0.757433056452*w_ode_1_3 + 0.597494499218*x_3 + 0.1*sin(x_3)  - 0.022651486531*x_4 + 0.497929842769*x_4 + -0.351506264963*(x_3*x_3*x_3 + x_3) + 0.50708661888*(ur_3*ur_3*ur_3 + ur_3) + -0.206720680911*(ur_1*ur_1*ur_1 + ur_1) + -0.833479026328*(ur_1*ur_1*ur_1 + ur_1) - -0.174337255305*ur_1 + 0.381676220423*ur_2;

w_ode_3_1*10 + 0.347711621581*(w_ode_3_1*w_ode_3_1*w_ode_3_1 + w_ode_3_1) + 0.285906007902*w_ode_3_2 + -0.808278538317*w_ode_3_3 + -0.627777932044*x_4 + 0.1*sin(x_4)  + 0.171234630281*x_3 + 0.1*sin(x_3)  + 0.382264815838*x_2 + 0.410666582812*(x_3*x_3*x_3 + x_3) + -0.0410207688198*(ur_3*ur_3*ur_3 + ur_3) + -0.279059287327*ur_2 + 0.1*sin(ur_2)  - -0.712779739225*ur_1 + 0.198001283493*(ur_1*ur_1*ur_1 + ur_1) - 0.643230239338*(ur_1*ur_1*ur_1 + ur_1) = 0;
w_ode_3_2*10 + -0.037401363361*w_ode_3_1 - -0.19947538103*w_ode_3_2 - -0.0652095837758*w_ode_3_3 + 0.1*sin(w_ode_3_3)  + 0.707763020011*x_1 + 0.1*sin(x_1)  + -0.482753945329*x_3 + 0.1*sin(x_3)  - 0.717191130471*x_3 + 0.730197877363*x_4 + 0.1*sin(x_4)  + -0.416473224221*(ur_2*ur_2*ur_2 + ur_2) - 0.35101472343*ur_3 + 0.1*sin(ur_3)  + -0.127557316725*(ur_1*ur_1*ur_1 + ur_1) + 0.170210789775*ur_1 + 0.0887130695405*ur_3 + 0.1*sin(ur_3)  = 0;
w_ode_3_3*10 + -0.450477509555*(w_ode_3_1*w_ode_3_1*w_ode_3_1 + w_ode_3_1) + 0.774378024451*w_ode_3_2 + 0.88257509024*(w_ode_3_3*w_ode_3_3*w_ode_3_3 + w_ode_3_3) + 0.308156742814*x_4 + 0.508379384048*x_4 - 0.0723346103084*x_2 + 0.1*sin(x_2)  + -0.295684455938*x_3 + -0.64179115935*ur_3 - -0.753738357004*ur_2 + -0.336940174625*ur_1 - 0.109847654411*(ur_2*ur_2*ur_2 + ur_2) + -0.375114548471*ur_2 + 0.1*sin(ur_2)  = 0;

der(x_3) = -0.862807451078*w_ode_3_1 - 0.0862702515104*w_ode_3_2 + -0.46830786361*(w_ode_3_3*w_ode_3_3*w_ode_3_3 + w_ode_3_3) + 0.745080368765*w_ode_2_1 + 0.1*sin(w_ode_2_1)  - -0.505607415804*w_ode_2_2 + -0.334274724945*(w_ode_2_3*w_ode_2_3*w_ode_2_3 + w_ode_2_3) + -0.77573823703*x_3 + 0.1*sin(x_3)  + -0.774630448753*x_4 - -0.630308140842*x_2 + 0.1*sin(x_2)  + 0.486634901035*x_4 + 0.0552024270643*(ur_3*ur_3*ur_3 + ur_3) + -0.499698812222*ur_2 + 0.606312922311*ur_1 - -0.233707393468*(ur_2*ur_2*ur_2 + ur_2) - 0.267283804682*ur_1;

w_ode_4_1*10 + 0.373260270163*w_ode_4_1 + 0.1*sin(w_ode_4_1)  - -0.0318556572471*(w_ode_4_2*w_ode_4_2*w_ode_4_2 + w_ode_4_2) - -0.995254216977*w_ode_4_3 + -0.613127160338*(x_3*x_3*x_3 + x_3) + 0.000894083470821*(x_2*x_2*x_2 + x_2) + 0.132009093214*x_3 - -0.728824429702*x_2 + 0.0777600559428*ur_2 + 0.741021519062*ur_1 + 0.716582429992*(ur_2*ur_2*ur_2 + ur_2) - 0.431904242634*ur_1 + 0.61336061664*ur_1 = 0;
w_ode_4_2*10 + 0.722919988632*(w_ode_4_1*w_ode_4_1*w_ode_4_1 + w_ode_4_1) - -0.0299964798121*w_ode_4_2 + 0.1*sin(w_ode_4_2)  + -0.844115378778*w_ode_4_3 + 0.1*sin(w_ode_4_3)  + -0.155777659887*(x_1*x_1*x_1 + x_1) + -0.0711893818143*x_2 + -0.638821878204*x_3 - -0.266134458053*(x_3*x_3*x_3 + x_3) + 0.566360523844*ur_2 + 0.1*sin(ur_2)  + -0.60940092565*ur_2 + 0.1*sin(ur_2)  + -0.192505486255*ur_1 + 0.1*sin(ur_1)  + -0.779861292114*ur_1 + 0.1*sin(ur_1)  + -0.880564513183*ur_1 + 0.1*sin(ur_1)  = 0;
w_ode_4_3*10 + -0.103953967722*(w_ode_4_1*w_ode_4_1*w_ode_4_1 + w_ode_4_1) - -0.897767808449*(w_ode_4_2*w_ode_4_2*w_ode_4_2 + w_ode_4_2) + -0.946673633025*w_ode_4_3 + 0.24490325326*(x_1*x_1*x_1 + x_1) + -0.896217572578*x_1 + 0.575678600997*(x_2*x_2*x_2 + x_2) - -0.398903690449*x_1 + 0.1*sin(x_1)  + 0.364797270825*ur_1 - -0.992687492001*ur_3 + 0.1*sin(ur_3)  + -0.659332103982*ur_2 + 0.1*sin(ur_2)  + 0.308623485412*ur_2 + 0.9476944172*(ur_1*ur_1*ur_1 + ur_1) = 0;

der(x_4) = 0.607177383879*w_ode_4_1 - -0.931576380397*w_ode_4_2 + 0.1*sin(w_ode_4_2)  - 0.893078914201*w_ode_4_3 + 0.1*sin(w_ode_4_3)  + -0.413132933019*w_ode_3_1 + -0.220273188542*(w_ode_3_2*w_ode_3_2*w_ode_3_2 + w_ode_3_2) - 0.85703880195*w_ode_3_3 + 0.1*sin(w_ode_3_3)  + 0.847006189584*(x_3*x_3*x_3 + x_3) + -0.541190364294*x_3 + -0.461085068868*x_4 + 0.1*sin(x_4)  - 0.211409284399*x_3 + -0.066143973291*ur_2 - -0.805825154184*ur_2 + 0.1*sin(ur_2)  - 0.284759656436*ur_1 - -0.1001913329*ur_3 - -0.332576811359*(ur_1*ur_1*ur_1 + ur_1);

w_output_1_1*20 + -0.855886381941*(w_output_1_1*w_output_1_1*w_output_1_1 + w_output_1_1) - -0.790006841146*(w_output_1_2*w_output_1_2*w_output_1_2 + w_output_1_2) + -0.838221820862*(w_output_1_3*w_output_1_3*w_output_1_3 + w_output_1_3) + 0.171114623328*x_1 + 0.1*sin(x_1)  + 0.934497508537*x_1 + 0.1*sin(x_1)  - -0.160756893382*x_1 - 0.577282382293*(x_3*x_3*x_3 + x_3) + -0.952010946588*ur_1 + 0.786567632184*ur_1 + 0.1*sin(ur_1)  + -0.55449474118*ur_1 - 0.283610902512*ur_3 - -0.307902806955*(ur_1*ur_1*ur_1 + ur_1) = 0;
w_output_1_2*20 + -0.10880689654*w_output_1_1 + 0.1*sin(w_output_1_1)  - 0.18879235452*w_output_1_2 + 0.0783641041451*(w_output_1_3*w_output_1_3*w_output_1_3 + w_output_1_3) + -0.85694587344*(x_3*x_3*x_3 + x_3) - -0.154296714304*(x_1*x_1*x_1 + x_1) - -0.571665938945*(x_2*x_2*x_2 + x_2) - -0.329593327103*(x_2*x_2*x_2 + x_2) + 0.749442560606*ur_1 - 0.862691085208*(ur_1*ur_1*ur_1 + ur_1) + 0.896108212935*ur_1 - -0.031618581806*ur_3 + 0.994603746944*ur_3 = 0;
w_output_1_3*20 + -0.415912599005*w_output_1_1 + -0.808265387591*w_output_1_2 + 0.038913534006*(w_output_1_3*w_output_1_3*w_output_1_3 + w_output_1_3) + -0.310422964868*x_1 - -0.425393787876*x_3 + 0.1*sin(x_3)  + -0.177838959637*x_2 + 0.1*sin(x_2)  + 0.525460747033*x_2 + -0.376120150983*(ur_3*ur_3*ur_3 + ur_3) - 0.0841478589567*(ur_3*ur_3*ur_3 + ur_3) - -0.42962627069*(ur_3*ur_3*ur_3 + ur_3) - 0.6142760341*ur_2 + 0.1*sin(ur_2)  + 0.613340340846*ur_1 + 0.1*sin(ur_1)  = 0;

w_output_2_1*20 + -0.737040778561*(w_output_2_1*w_output_2_1*w_output_2_1 + w_output_2_1) - -0.668541193752*w_output_2_2 + 0.1*sin(w_output_2_2)  + 0.539994653957*(w_output_2_3*w_output_2_3*w_output_2_3 + w_output_2_3) + -0.629921373148*x_4 + 0.1*sin(x_4)  + -0.323462041683*x_4 + 0.1*sin(x_4)  - -0.812364735454*x_4 + 0.1*sin(x_4)  + 0.604254014769*(x_1*x_1*x_1 + x_1) + 0.825104501268*ur_1 + -0.728669140582*ur_1 - 0.0176603756931*ur_2 - -0.440813287845*ur_2 + 0.1*sin(ur_2)  + 0.286186517185*ur_3 = 0;
w_output_2_2*20 + 0.812322563828*(w_output_2_1*w_output_2_1*w_output_2_1 + w_output_2_1) - 0.85723866314*w_output_2_2 - -0.171144852474*(w_output_2_3*w_output_2_3*w_output_2_3 + w_output_2_3) + 0.0941330358619*(x_1*x_1*x_1 + x_1) + -0.0902166027063*x_1 + 0.918524809626*x_3 + 0.1*sin(x_3)  + 0.0439968412781*(x_4*x_4*x_4 + x_4) + 0.149017387595*(ur_3*ur_3*ur_3 + ur_3) + -0.440301004268*ur_3 - -0.795085051131*ur_3 + 0.0295859647841*ur_2 - 0.28710830879*ur_1 + 0.1*sin(ur_1)  = 0;
w_output_2_3*20 + 0.841418122438*w_output_2_1 + 0.1*sin(w_output_2_1)  + 0.656353270957*w_output_2_2 + 0.1*sin(w_output_2_2)  + 0.899827376573*w_output_2_3 + -0.49955212454*x_2 + -0.540495932746*x_2 + 0.1*sin(x_2)  + 0.0524994599094*x_2 - 0.262233731726*x_1 + -0.034314446721*ur_1 + 0.1*sin(ur_1)  - -0.905725789448*ur_1 + 0.1*sin(ur_1)  - -0.711566505583*ur_3 + 0.985633097102*ur_1 - -0.715574810031*ur_1 + 0.1*sin(ur_1)  = 0;

w_output_3_1*20 + 0.518934259215*w_output_3_1 + 0.1*sin(w_output_3_1)  + 0.645386235874*w_output_3_2 + 0.921531128168*(w_output_3_3*w_output_3_3*w_output_3_3 + w_output_3_3) + -0.438464625113*x_2 + 0.1*sin(x_2)  + -0.746185371524*(x_1*x_1*x_1 + x_1) - -0.846072704575*x_2 + 0.1*sin(x_2)  - 0.993797781207*x_4 + -0.373456396569*ur_1 + 0.1*sin(ur_1)  + 0.496351970048*ur_2 - -0.0718636581604*(ur_3*ur_3*ur_3 + ur_3) + 0.0688718476333*ur_2 + 0.188621674412*ur_3 = 0;
w_output_3_2*20 + 0.696687903219*w_output_3_1 + 0.1*sin(w_output_3_1)  - 0.680085196481*w_output_3_2 + 0.1*sin(w_output_3_2)  + -0.59528481766*w_output_3_3 + 0.1*sin(w_output_3_3)  + -0.972153810293*x_4 - 0.983120509519*x_2 - 0.532073591279*x_4 + 0.1*sin(x_4)  - -0.117618019494*x_1 + 0.1*sin(x_1)  + -0.283120353483*(ur_2*ur_2*ur_2 + ur_2) - 0.872302224398*ur_1 - -0.426412359236*ur_2 + -0.753641641109*(ur_2*ur_2*ur_2 + ur_2) - -0.31797336446*(ur_1*ur_1*ur_1 + ur_1) = 0;
w_output_3_3*20 + -0.435215183575*w_output_3_1 + -0.0442789892178*(w_output_3_2*w_output_3_2*w_output_3_2 + w_output_3_2) - 0.973061958258*(w_output_3_3*w_output_3_3*w_output_3_3 + w_output_3_3) + 0.694958472409*x_2 + 0.708964040603*(x_3*x_3*x_3 + x_3) - -0.266768701166*x_1 + 0.1*sin(x_1)  - 0.767696307862*(x_2*x_2*x_2 + x_2) + -0.20197487713*(ur_3*ur_3*ur_3 + ur_3) - 0.750257434014*(ur_3*ur_3*ur_3 + ur_3) + -0.560174942016*(ur_2*ur_2*ur_2 + ur_2) - -0.72096361391*ur_1 + 0.1*sin(ur_1)  + -0.434040990519*ur_2 + 0.1*sin(ur_2)  = 0;

w_other_1_1*10 + 0.0775894631926*w_other_1_1 - 0.474826788366*w_other_1_2 - 0.826093885497*(w_other_1_3*w_other_1_3*w_other_1_3 + w_other_1_3) + -0.0492950210137*x_3 + -0.620177833478*x_1 - -0.830324568886*x_4 + 0.1*sin(x_4)  + -0.985031239834*x_2 + 0.257318704571*(ur_1*ur_1*ur_1 + ur_1) + -0.805923154348*ur_1 - -0.832913934225*(ur_2*ur_2*ur_2 + ur_2) - 0.983555694239*ur_2 + 0.1*sin(ur_2)  + -0.0401204390426*(ur_2*ur_2*ur_2 + ur_2) = 0;
w_other_1_2*10 + 0.788816602441*w_other_1_1 + -0.162476094342*(w_other_1_2*w_other_1_2*w_other_1_2 + w_other_1_2) - -0.596131613129*(w_other_1_3*w_other_1_3*w_other_1_3 + w_other_1_3) + 0.0474519020232*(x_1*x_1*x_1 + x_1) + -0.535529735374*(x_3*x_3*x_3 + x_3) - 0.0781025647526*x_1 + 0.1*sin(x_1)  - 0.32289849163*(x_4*x_4*x_4 + x_4) + 0.23992807445*(ur_1*ur_1*ur_1 + ur_1) - 0.819913604627*ur_1 - -0.59283941318*ur_3 + 0.1*sin(ur_3)  + -0.375819807803*ur_1 + 0.1*sin(ur_1)  - -0.567858276014*ur_2 = 0;
w_other_1_3*10 + 0.875282547724*w_other_1_1 + 0.1*sin(w_other_1_1)  - -0.205704020825*w_other_1_2 + 0.1*sin(w_other_1_2)  + -0.924575785891*(w_other_1_3*w_other_1_3*w_other_1_3 + w_other_1_3) + -0.197369137899*(x_2*x_2*x_2 + x_2) + -0.498589614844*x_4 + 0.1*sin(x_4)  - -0.319585744556*x_4 + 0.1*sin(x_4)  + -0.11564792435*(x_1*x_1*x_1 + x_1) + -0.648478795827*ur_1 + 0.0790701869806*(ur_3*ur_3*ur_3 + ur_3) - -0.115318754697*ur_1 + 0.1*sin(ur_1)  - 0.719265050547*(ur_3*ur_3*ur_3 + ur_3) - -0.463055066471*ur_2 = 0;

w_other_2_1*10 + 0.371332712395*w_other_2_1 + 0.1*sin(w_other_2_1)  - 0.972240783055*(w_other_2_2*w_other_2_2*w_other_2_2 + w_other_2_2) - -0.03374396625*w_other_2_3 + 0.1*sin(w_other_2_3)  + -0.784697050616*(x_3*x_3*x_3 + x_3) - -0.0444029177829*(x_2*x_2*x_2 + x_2) - -0.106691652912*(x_3*x_3*x_3 + x_3) - 0.647713938872*x_3 + 0.1*sin(x_3)  + 0.769204203614*(ur_1*ur_1*ur_1 + ur_1) - 0.671926586683*ur_3 + -0.978360169784*ur_2 - -0.298666247386*(ur_1*ur_1*ur_1 + ur_1) - -0.500334467063*ur_3 = 0;
w_other_2_2*10 + 0.12501902631*(w_other_2_1*w_other_2_1*w_other_2_1 + w_other_2_1) + 0.107894274027*w_other_2_2 + 0.1*sin(w_other_2_2)  - -0.654928258938*(w_other_2_3*w_other_2_3*w_other_2_3 + w_other_2_3) + -0.890394902132*(x_1*x_1*x_1 + x_1) + 0.0101944009291*x_2 + 0.1*sin(x_2)  + 0.0750312822653*x_3 - 0.0310521768863*(x_1*x_1*x_1 + x_1) + 0.895936699362*(ur_1*ur_1*ur_1 + ur_1) + -0.475458825092*ur_1 + 0.142686959807*(ur_1*ur_1*ur_1 + ur_1) + -0.55408435692*ur_3 - 0.466888954389*ur_1 = 0;
w_other_2_3*10 + -0.802890213303*w_other_2_1 - -0.549260914559*(w_other_2_2*w_other_2_2*w_other_2_2 + w_other_2_2) - -0.346463399701*w_other_2_3 + -0.255242215099*x_1 - 0.00830290564515*x_3 + 0.608559033721*x_2 + 0.1*sin(x_2)  - 0.171283809856*(x_3*x_3*x_3 + x_3) + 0.00980363382217*ur_1 - 0.45474153227*(ur_1*ur_1*ur_1 + ur_1) + 0.113288187439*ur_2 - -0.594652636081*ur_1 + 0.1*sin(ur_1)  - 0.478913248685*(ur_3*ur_3*ur_3 + ur_3) = 0;

w_other_3_1*10 + 0.476964641939*w_other_3_1 + 0.1*sin(w_other_3_1)  - 0.337271240577*(w_other_3_2*w_other_3_2*w_other_3_2 + w_other_3_2) + -0.726427985925*(w_other_3_3*w_other_3_3*w_other_3_3 + w_other_3_3) + 0.570426605918*(x_4*x_4*x_4 + x_4) + 0.98804895078*(x_1*x_1*x_1 + x_1) + 0.401925859254*x_1 + 0.1*sin(x_1)  + 0.397260865797*x_1 + 0.1*sin(x_1)  + 0.60435231345*(ur_1*ur_1*ur_1 + ur_1) - -0.109798775083*ur_2 + -0.550828956945*(ur_1*ur_1*ur_1 + ur_1) - -0.309387799876*ur_3 + 0.1*sin(ur_3)  + -0.808215880462*ur_1 + 0.1*sin(ur_1)  = 0;
w_other_3_2*10 + 0.145679743806*(w_other_3_1*w_other_3_1*w_other_3_1 + w_other_3_1) - -0.419965563766*w_other_3_2 + 0.1*sin(w_other_3_2)  + -0.321998712073*w_other_3_3 + 0.1*sin(w_other_3_3)  + 0.324663458736*x_3 - -0.146856492209*x_2 + 0.1*sin(x_2)  + 0.58885762769*(x_4*x_4*x_4 + x_4) + 0.853252782511*(x_3*x_3*x_3 + x_3) + -0.267507649569*ur_2 + -0.00101290541639*(ur_2*ur_2*ur_2 + ur_2) + 0.849233579189*(ur_1*ur_1*ur_1 + ur_1) + -0.052899560012*ur_3 + 0.1*sin(ur_3)  - 0.738072238565*ur_1 = 0;
w_other_3_3*10 + -0.90413470053*w_other_3_1 + -0.0547223315922*w_other_3_2 + 0.1*sin(w_other_3_2)  + -0.734521920845*(w_other_3_3*w_other_3_3*w_other_3_3 + w_other_3_3) + -0.616890680232*x_1 + 0.1*sin(x_1)  - 0.0617693923182*x_4 - 0.261082115241*x_1 + 0.1*sin(x_1)  - 0.0248991378308*x_4 + 0.42187501986*(ur_1*ur_1*ur_1 + ur_1) + -0.0691676088665*(ur_1*ur_1*ur_1 + ur_1) + -0.388762705308*ur_3 + -0.0537019558584*ur_3 + 0.1*sin(ur_3)  + 0.301087338652*ur_2 = 0;

end BlockOdeJacTest;

