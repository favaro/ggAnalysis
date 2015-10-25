import FWCore.ParameterSet.Config as cms

process = cms.Process("ggkIT")

#process.load("FWCore.MessageLogger.MessageLogger_cfi")
#process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32(1000)
#process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

process.load("Configuration.StandardSequences.GeometryDB_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = cms.string('START53_V7A::All')
process.load("Configuration.StandardSequences.MagneticField_cff")

process.load('Configuration.StandardSequences.Reconstruction_cff')

process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(1000)
            )

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
        #'root://xrootd.ba.infn.it//store/mc/Summer12_DR53X/JJHiggs0PToGG_M-125p6_8TeV-JHUGenV4-pythia6-tauola/AODSIM/PU_RD1_START53_V7N-v1/00000/021391E4-6803-E411-BE5E-002590A7A2E0.root',
        'root://xrootd.ba.infn.it//store/mc/Summer12_DR53X/VBFHiggs0PToGG_M-125p6_8TeV-JHUGenV4-pythia6-tauola/AODSIM/PU_RD1_START53_V7N-v3/00000/0A2798DF-7D16-E411-96B9-0025901D4AFE.root',
        'root://xrootd.ba.infn.it//store/mc/Summer12_DR53X/VBFHiggs0PToGG_M-125p6_8TeV-JHUGenV4-pythia6-tauola/AODSIM/PU_RD1_START53_V7N-v3/00000/0A787126-0D16-E411-A425-003048CF6336.root'
        #'root://xrootd.ba.infn.it//store/mc/Summer11LegDR/VBFHiggs0PToGG_M-125p6_7TeV-JHUGenV4-pythia6-tauola/AODSIM/PU_S13_START53_LV6-v1/00000/06BBC13C-4001-E411-8D9F-002590AC4BF6.root',
        #'root://xrootd.ba.infn.it//store/mc/Summer11LegDR/VBFHiggs0PToGG_M-125p6_7TeV-JHUGenV4-pythia6-tauola/AODSIM/PU_S13_START53_LV6-v1/00000/0EABEA2D-4701-E411-8BF8-00266CF2D5C4.root',
        #'root://xrootd.ba.infn.it//store/mc/Summer11LegDR/VBFHiggs0PToGG_M-125p6_7TeV-JHUGenV4-pythia6-tauola/AODSIM/PU_S13_START53_LV6-v1/00000/107122FC-3C01-E411-993B-0025901D4C3C.root',
        #'root://xrootd.ba.infn.it//store/mc/Summer11LegDR/VBFHiggs0PToGG_M-125p6_7TeV-JHUGenV4-pythia6-tauola/AODSIM/PU_S13_START53_LV6-v1/00000/1211AEC2-4301-E411-9174-0025907DC9BE.root'
        #'root://stormgf2.pi.infn.it:1094//store/mc/Summer11LegDR/VBFHiggs0PToGG_M-125p6_7TeV-JHUGenV4-pythia6-tauola/AODSIM/PU_S13_START53_LV6-v1/00000/06BBC13C-4001-E411-8D9F-002590AC4BF6.root'
        #'file:/data4/cmkuo/testfiles/GluGluToHToGG_M-126_8TeV-powheg-pythia6_PU_RD1_START53_V7N-v1_02D0B20F-23D2-E211-8C14-0026189438A9.root'
        #    'file:/data4/cmkuo/testfiles/hzg_jjg_VBFH_125.root'
        ),
                            noEventSort = cms.untracked.bool(True),
                            duplicateCheckMode = cms.untracked.string('noDuplicateCheck')
                            )

process.load("PhysicsTools.PatAlgos.patSequences_cff")
process.patJets.discriminatorSources = cms.VInputTag(
    cms.InputTag("combinedSecondaryVertexBJetTags"),
    cms.InputTag("combinedSecondaryVertexMVABJetTags"),
    cms.InputTag("jetBProbabilityBJetTags"),
    cms.InputTag("jetProbabilityBJetTags"),
    cms.InputTag("simpleSecondaryVertexHighEffBJetTags"),
    cms.InputTag("simpleSecondaryVertexHighPurBJetTags"),
    #cms.InputTag("softPFElectronBJetTags"),
   #cms.InputTag("softElectronByIP3dBJetTags"),
    #cms.InputTag("softPFMuonBJetTags"),
    #cms.InputTag("softMuonByPtBJetTags"),
    #cms.InputTag("softMuonByIP3dBJetTags"),
    cms.InputTag("trackCountingHighEffBJetTags"),
    cms.InputTag("trackCountingHighPurBJetTags"),
)

# Trigger matching
process.load("ggAnalysis.ggNtuplizer.ggPatTriggerMatching_cff")

# Jets
process.load('JetMETCorrections.Configuration.DefaultJEC_cff')
process.patJetCorrFactors.useRho = cms.bool(True)

process.ak5PFJets.doAreaFastjet = True
process.patJets.addTagInfos = cms.bool(True)

# Taus
from PhysicsTools.PatAlgos.tools.tauTools import *
process.load("RecoTauTag.Configuration.RecoPFTauTag_cff")
process.cleanPatTaus.preselection = cms.string(' tauID("decayModeFinding") > 0.5 ')
process.cleanPatTaus.finalCut     = cms.string(' pt > 15.0 & abs(eta) < 2.5 ')
process.load("ggAnalysis.ggNtuplizer.ggTau_cff")

#process.patJetCorrFactors.levels = ['L1FastJet', 'L2Relative', 'L3Absolute']
#process.patJetCorrFactors.rho = cms.InputTag('kt6PFJets25','rho')

from PhysicsTools.PatAlgos.tools.jetTools import *
addJetCollection(process,
                 cms.InputTag('ak5PFJets'),
                 'AK5', 'PF',
                 doJTA        = True,
                 doBTagging   = True,
                 jetCorrLabel = ('AK5PF', cms.vstring(['L1FastJet', 'L2Relative', 'L3Absolute'])),
                 doType1MET   = False,
                 doL1Cleaning = False,
                 doL1Counters = False,
                 genJetCollection = cms.InputTag("ak5GenJets"),
                 doJetID      = False
                 )

# load the coreTools of PAT
from PhysicsTools.PatAlgos.tools.metTools import *
addTcMET(process, 'TC')
addPfMET(process, 'PF')

process.load("JetMETCorrections.Type1MET.pfMETCorrectionType0_cfi")
process.pfType0pfcp1CorrectedMet = process.pfType1CorrectedMet.clone()
process.pfType0pfcp1CorrectedMet.srcType1Corrections = cms.VInputTag(
    cms.InputTag('pfMETcorrType0'),
    cms.InputTag('pfJetMETcorr', 'type1')
    )

process.patMETsType0pfcp1PF = process.patMETsPF.clone()
process.patMETsType0pfcp1PF.metSource = cms.InputTag("pfType0pfcp1CorrectedMet")

process.produceType0MET = cms.Sequence(
    process.pfType0pfcp1CorrectedMet*
    process.patMETsType0pfcp1PF
    )

#process.patJetGenJetMatch.matched = cms.InputTag('iterativeCone5GenJets')

process.cleanPatPhotons.checkOverlaps.electrons.requireNoOverlaps = cms.bool(False)

# PF isolations for electrons and muons
from CommonTools.ParticleFlow.Tools.pfIsolation import setupPFElectronIso, setupPFPhotonIso
process.eleIsoSequence = setupPFElectronIso(process, 'gsfElectrons')
process.phoIsoSequence = setupPFPhotonIso(process, 'photons')

process.load("ggAnalysis.ggNtuplizer.ggNtuplizer_crab_cfi")
process.ggNtuplizer.jetSrc = cms.InputTag("selectedPatJetsAK5PF")
process.ggNtuplizer.triggerResults = cms.InputTag("TriggerResults::HLT")
process.ggNtuplizer.getBlocks=cms.bool(False)
process.ggNtuplizer.useAllPF=cms.bool(False)
process.ggNtuplizer.dumpTrks=cms.bool(True)
process.ggNtuplizer.dumpSubJets=cms.bool(True)
process.TFileService = cms.Service("TFileService", fileName = cms.string('ggtree_mc.root'))

# electron energy regression
process.load("EgammaAnalysis.ElectronTools.electronRegressionEnergyProducer_cfi")
process.eleRegressionEnergy.energyRegressionType = cms.uint32(2)

process.load("Configuration.StandardSequences.Services_cff")
process.RandomNumberGeneratorService = cms.Service("RandomNumberGeneratorService",
                                                  calibratedPatElectrons = cms.PSet(
    initialSeed = cms.untracked.uint32(1),
    engineName = cms.untracked.string('TRandom3')
    ),
                                                   )

process.load("EgammaAnalysis.ElectronTools.calibratedPatElectrons_cfi")
process.calibratedPatElectrons.isMC = cms.bool(True)
process.calibratedPatElectrons.inputDataset = cms.string("Summer12_LegacyPaper")
process.calibratedPatElectrons.correctionsType = cms.int32(2)
process.calibratedPatElectrons.combinationType = cms.int32(3)

process.load("ggAnalysis.ggNtuplizer.ggRhoFastJet_cff")
process.load("ggAnalysis.ggNtuplizer.ggMergedJets_mc_cff")
process.load("ggAnalysis.ggNtuplizer.ggEleID_cff")
process.load("ggAnalysis.ggNtuplizer.ggBoostedEleModIso_cff")

process.patElectrons.userIsolation.user = cms.VPSet(
    cms.PSet(src = cms.InputTag("modElectronIso","track")),
    cms.PSet(src = cms.InputTag("modElectronIso","ecal")),
    cms.PSet(src = cms.InputTag("modElectronIso","hcalDepth1"))
    )

process.patElectrons.electronIDSources = cms.PSet(
    mvaTrigV0 = cms.InputTag("mvaTrigV0"),
    mvaNonTrigV0 = cms.InputTag("mvaNonTrigV0")
    )

# Output definition
#process.output = cms.OutputModule("PoolOutputModule",
#                                  fileName = cms.untracked.string('output.root')
#)

process.p = cms.Path(
    process.fjSequence*
    process.ak5PFJets*
    process.pfNoPileUpSequence* ###########
    process.pfParticleSelectionSequence*
    process.ggBoostedEleModIsoSequence*
    process.eleMVAID*
    process.type0PFMEtCorrection*
    process.patDefaultSequence*
    process.produceType0MET*
    process.eleIsoSequence*
    process.phoIsoSequence*
    process.ca8Jets* ###########
    process.QuarkGluonTagger*
    process.eleRegressionEnergy*
    process.calibratedPatElectrons*
    process.ggTriggerSequence*
    process.recoTauClassicHPSSequence*
    process.ggNtuplizer)

#process.out_step = cms.EndPath(process.output)
