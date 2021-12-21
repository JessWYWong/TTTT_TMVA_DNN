#!/usr/bin/env python

#input variables
varList = {}

# EDIT ME 
bruxUserName = "wwong"
lpcUserName = "wywong"
eosUserName = "wiwong"
date = "012020"
#date = "10072020" # production date
#date = "02182021"

step2Sample = {
  "2017": "FWLJMET102X_3lep2017_wywong_012020_step1_FRv5_PRv4_ANv8_uFRupdate_hadds_step2" ,
  "2018": "FWLJMET102X_1lep2018_Oct2019_4t_{}_step2".format( date )
}

step3Sample = { year: "FWLJMET102X_3lep{}_wywong_{}_step3".format( str( year ), date ) for year in step2Sample.keys() }

step2DirBRUX = { year: "/isilon/data/users/wwong/{}/".format( step2Sample[ year ] ) for year in step2Sample.keys() }

step2DirLPC = { year: "/uscms_data/d3/wywong/DNN/CMSSW_9_4_6_patch1/src/TTTT_TMVA_DNN/{}/".format( step2Sample[ year ] ) for year in step2Sample.keys() }

step3DirLPC = { year: "~/nobackup/DNN/CMSSW_9_4_6_patch1/src/TTTT_TMVA_DNN/{}/".format( step3Sample[ year ] ) for year in step2Sample.keys() }

step2DirEOS = { year: "root://cmseos.fnal.gov///store/user/{}/{}/".format( eosUserName, step2Sample[ year ] ) for year in step2Sample.keys() }

step3DirEOS = { year: "root://cmseos.fnal.gov///store/user/{}/{}/".format( eosUserName, step3Sample[ year ] ) for year in step2Sample.keys() }

# full signal sample to be used in training
sig_training = {
  "2017": [ "TprimeTprime_M-1000_TuneCP5_13TeV-madgraph-pythia8_BWBW_hadd.root" ],
  "2018": [ "TTTT_TuneCP5_13TeV-amcatnlo-pythia8_hadd.root" ]
}

# full background samples to be used in training
bkg_training = {
  "2017": [
    "TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8_hadd.root",
    "TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8_hadd.root"
  ],
  "2018": [
  ]
}

# all samples for step3, ( Name, # Processed MC events, xsec [pb] )

shift_keys = {
  "": ""
}

all_samples = {
  "2017": {
    "TTM1000BWBW":"TprimeTprime_M-1000_TuneCP5_13TeV-madgraph-pythia8_BWBW_hadd.root",

    "TTWl":"TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8_hadd.root",
    "TTZl":"TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8_hadd.root",

    "WZ":"WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8_hadd.root",
    "ZZ":"ZZTo4L_13TeV_powheg_pythia8_hadd.root",

    "WWW":"WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8_hadd.root",
    "WWZ":"WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8_hadd.root",
    "WZZ_3L":"WZZTo3L1Nu2Q_4f_TuneCP5_13TeV_amcatnlo_pythia8_hadd.root",
    "WZZ_4L":"WZZ_ZTo2L_WToAll_4f_TuneCP5_13TeV_amcatnlo_pythia8_hadd.root",
    "ZZZ":"ZZZ_TuneCP5_13TeV-amcatnlo-pythia8_hadd.root",
    "TT2l":"TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8_hadd.root",

    "DataEE": "DoubleEG_hadd.root",
    "DataEM": "MuonEGR_hadd.root",
    "DataMM": "DoubleMuon_hadd.root"
  },
  "2018": {
  }
}

'''
for jj in [ "TT1b", "TT2b", "TTbb", "TTcc", "TTjj" ]:
  for shift in [ "", "UEdn", "UEup", "HDAMPdn", "HDAMPup" ]:
 
   if shift == "":
      # 2017 nominal ttbar samples
      all_samples[ "2017" ][ "TTJets2L2nu{}{}".format( shift, jj ) ] = "TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8_{}_hadd.root".format( jj.lower() )
      all_samples[ "2018" ][ "TTJets2L2nu{}{}".format( shift, jj ) ] = "TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8_{}_hadd.root".format( jj.lower() )
      if jj == "TTjj":
        #for n in [ "1", "2", "3", "4", "5" ]:
        #  all_samples[ "2017" ][ "TTJetsSemiLepNjet0{}{}{}".format( shift, jj, n ) ] = "TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8_HT0Njet0_{}_{}_hadd.root".format( jj, n )
        for n in [ "1", "2" ]:
          all_samples[ "2018" ][ "TTJetsSemiLepNjet0{}{}{}".format( shift, jj, n ) ] = "TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8_HT0Njet0_{}_{}_hadd.root".format( jj, n )
    elif "UE" in shift:
      all_samples[ "2017" ][ "TTJets2L2nu{}{}".format( shift, jj ) ] = "TTTo2L2Nu_TuneCP5{}_PSweights_13TeV-powheg-pythia8_{}_hadd.root".format( shift_keys[ shift ], jj.lower() )
    elif "HDAMP" in shift:
      all_samples[ "2017" ][ "TTJets2L2nu{}{}".format( shift, jj ) ] = "TTTo2L2Nu_{}_TuneCP5_PSweights_13TeV-powheg-pythia8_{}_hadd.root".format( shift_keys[ shift ], jj.lower() )
'''

#[<variable in trees>, <variable name for axes and titles>, <unit>]

varList["DNN"] = [
  ("AK4HTpMETpLepPt", "S_{T} [GeV]" , 0, 4000, 101),
  ("minMleppBjet", "min[M(l,b)] [GeV]", 0, 1000, 101), 
  ("BJetLeadPt", "p_{T}{b_{1}) [GeV]", 0, 2000, 101),
  ("AK4HT", "H_{T} [GeV]", 0, 3000, 121),
  ("corr_met_MultiLepCalc", "p_{T}^{miss} [GeV]", 0, 1500, 51),
  ("deltaRlepJetInMinMljet", "#DeltaR(l,j) with min M(l, j)", 0, 6.0, 51), # loop over all AK4 jets and lep
  ("deltaPhilepJetInMinMljet", "#DeltaPhi(l,j) with min M(l, j)", -4, 4, 51), # loop over all AK4 jets and lep
  ("deltaRlepbJetInMinMlb", "#DeltaR(l,b) with min M(l, b)", 0, 6.0, 51), # loop over all b-tagged AK4 jets and lep
  ("deltaPhilepbJetInMinMlb", "#DeltaPhi(l,b) with min M(l, b)", -4, 4, 51), # loop over all b-tagged AK4 jets and lep
  # new var with similar physics meaning
  ("AllLeptonPt_PtOrderedOnly[0]", "Leading Lepton p_{T} [GeV]", 0, 600, 121), # leading lepton pT
  ("AK4JetPt_MultiLepCalc_PtOrdered[0]", "p_{T}(j_{1}) [GeV]", 0, 2500, 101),
  ("AK4JetPt_MultiLepCalc_PtOrdered[1]", "p_{T}(j_{2}) [GeV]", 0, 2500, 101),
  ("Mlll", "M(l,l,l) [GeV]", 0, 2000, 101),
  ("Mll_sameFlavorOS", "M(l,l)_{OS,same Flav} [GeV]", 0, 1000, 101),
  ("minDR_lepJet", "min[#DeltaR(l,j)]", 0, 6.0, 51),
  ("minDR_lep1Jet", "min[#DeltaR(l_{1},j)]", 0, 6.0, 51),
  ("minDR_lep2Jet", "min[#DeltaR(l_{2},j)]", 0, 6.0, 51),
  ("minDR_lep3Jet", "min[#DeltaR(l_{3},j)]", 0, 6.0, 51),
  ("AK4JetDeepCSVb_MultiLepCalc_PtOrdered[0]+AK4JetDeepCSVbb_MultiLepCalc_PtOrdered[0]", "DeepCSV(1stDeepCSVJet)", -2, 1.5, 51),
  ("AK4JetDeepCSVb_MultiLepCalc_PtOrdered[1]+AK4JetDeepCSVbb_MultiLepCalc_PtOrdered[1]", "DeepCSV(2ndDeepCSVJet)", -2, 1.5, 51),
  ("NJets_MultiLepCalc", "AK4 jet multiplicity", 0, 15, 16),
  ("NJetsBTagwithSF_MultiLepCalc", "Deep Flav. b-tagged jet multiplicity", 0, 10, 11) # use Deep Flav. not DeepCSV in analysis 
]

# weight event count

weightStr = "TrigEffWeight * xsecEff * pileupWeight * L1NonPrefiringProb_CommonCalc * 1 * isoSF * lepIdSF * EGammaGsfSF * MuTrkSF" + \
            " * ((MCWeight_MultiLepCalc)/abs(MCWeight_MultiLepCalc))"

sigweightStr = "TrigEffWeight * xsecEff * pileupWeight * L1NonPrefiringProb_CommonCalc * 1 * isoSF * lepIdSF * EGammaGsfSF * MuTrkSF" + \
               " * (MCWeight_MultiLepCalc) * pdfWeights4LHC[0]"
#weightStr = "triggerXSF * pileupWeight * lepIdSF * EGammaGsfSF * isoSF * L1NonPrefiringProb_CommonCalc * " + \ 
#            "(MCWeight_MultiLepCalc / abs(MCWeight_MultiLepCalc) ) * xsecEff * tthfWeight * njetsWeight * btagCSVWeight * btagCSVRenormWeight"

# general cut, add selection based cuts in training scripts
cuts = {
  "ST": 300,
  "MET": 20,
  "bJet1Pt": 50, 
  "ptRel": 8,
  "minDRlepJet": 0,
#  "nJet": 3,
#  "nbJet": 1,
  "MllOS": 20,
}

base_cut =  "(( DataPastTrigger_dilep == 1 && isPassTrilepton == 1 ) || (MCPastTrigger_dilep == 1 && isPassTrilepton == 1))"
base_cut += " && AK4HTpMETpLepPt >= {} && corr_met_MultiLepCalc >= {}".format( cuts[ "ST" ], cuts[ "MET" ])
base_cut += " && BJetLeadPt >= {}".format( cuts[ "bJet1Pt" ])
base_cut += " && ( ( ptRel_minDRlep1Jet > {} && minDR_lep1Jet > {} )".format( cuts[ "ptRel" ], cuts[ "minDRlepJet" ] )
base_cut += " && ( ptRel_minDRlep2Jet > {} && minDR_lep2Jet > {} )".format( cuts[ "ptRel" ], cuts[ "minDRlepJet" ] )
base_cut += " && ( ptRel_minDRlep3Jet > {} && minDR_lep3Jet > {} ) )".format( cuts[ "ptRel" ], cuts[ "minDRlepJet" ] )
#base_cut += " && NJets_MultiLepCalc == {} && NJetsBTagwithSF_MultiLepCalc>= {}".format( cuts[ "nJet" ], cuts[ "nbJet" ] )
base_cut += " && ( (MllOS_allComb[0] > {} || MllOS_allComb[0] < 0)".format( cuts[ "MllOS" ])
base_cut += " && (MllOS_allComb[1] > {} || MllOS_allComb[1] < 0)".format( cuts[ "MllOS" ])
base_cut += " && (MllOS_allComb[2] > {} || MllOS_allComb[2] < 0)".format( cuts[ "MllOS" ])
base_cut += " && (MllOS_allComb[3] > {} || MllOS_allComb[3] < 0)".format( cuts[ "MllOS" ])
base_cut += " && (MllOS_allComb[4] > {} || MllOS_allComb[4] < 0)".format( cuts[ "MllOS" ])
base_cut += " && (MllOS_allComb[5] > {} || MllOS_allComb[5] < 0)".format( cuts[ "MllOS" ])
base_cut += " && (MllOS_allComb[6] > {} || MllOS_allComb[6] < 0)".format( cuts[ "MllOS" ])
base_cut += " && (MllOS_allComb[7] > {} || MllOS_allComb[7] < 0)".format( cuts[ "MllOS" ])
base_cut += " && (MllOS_allComb[8] > {} || MllOS_allComb[8] < 0)".format( cuts[ "MllOS" ])
base_cut += " && (MllOS_allComb[9] > {} || MllOS_allComb[9] < 0)".format( cuts[ "MllOS" ])
base_cut += " && (MllOS_allComb[10] > {} || MllOS_allComb[10] < 0)".format( cuts[ "MllOS" ])
base_cut += " && (MllOS_allComb[11] > {} || MllOS_allComb[11] < 0)".format( cuts[ "MllOS" ])
base_cut += " && (MllOS_allComb[12] > {} || MllOS_allComb[12] < 0)".format( cuts[ "MllOS" ])
base_cut += " && (MllOS_allComb[13] > {} || MllOS_allComb[13] < 0)".format( cuts[ "MllOS" ])
base_cut += " && (MllOS_allComb[14] > {} || MllOS_allComb[14] < 0) )".format( cuts[ "MllOS" ])

