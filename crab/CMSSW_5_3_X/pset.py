# Auto generated configuration file
# using:
# Revision: 1.381.2.28
# Source: /local/reps/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v
# with command line options: MinBias_8TeV_cfi --conditions auto:startup -s GEN,SIM --datatier GEN-SIM -n 10 --relval 25000,250 --eventcontent RAWSIM --fileout file:step1.root
# Testing cmsbot crab setup
# Testing cmsbot crab setup
def cmsbot_crab_test():
    import sys

    try:
        from subprocess import getstatusoutput
    except:
        from commands import getstatusoutput
    from FWCore.Version.cmsbot_crab_test import CMSBOT_CRAB_TEST

    cmsbot_exit, cmsbot_out = getstatusoutput("cmsbot_crab_test.sh")
    print("CMSBOT Crab Test:", CMSBOT_CRAB_TEST, cmsbot_exit, cmsbot_out)
    if cmsbot_exit or (cmsbot_out != "OK") or (CMSBOT_CRAB_TEST != "OK"):
        sys.exit(1)


cmsbot_crab_test()


import FWCore.ParameterSet.Config as cms

process = cms.Process("SIM")

# import of standard configurations
process.load("Configuration.StandardSequences.Services_cff")
process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("Configuration.EventContent.EventContent_cff")
process.load("SimGeneral.MixingModule.mixNoPU_cfi")
process.load("Configuration.StandardSequences.GeometryRecoDB_cff")
process.load("Configuration.StandardSequences.GeometrySimDB_cff")
process.load("Configuration.StandardSequences.MagneticField_38T_cff")
process.load("Configuration.StandardSequences.Generator_cff")
process.load("IOMC.EventVertexGenerators.VtxSmearedRealistic8TeVCollision_cfi")
process.load("GeneratorInterface.Core.genFilterSummary_cff")
process.load("Configuration.StandardSequences.SimIdeal_cff")
process.load("Configuration.StandardSequences.EndOfProcess_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")

process.maxEvents = cms.untracked.PSet(input=cms.untracked.int32(10))

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet()

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version=cms.untracked.string("$Revision: 1.381.2.28 $"),
    annotation=cms.untracked.string("MinBias_8TeV_cfi nevts:10"),
    name=cms.untracked.string("PyReleaseValidation"),
)

# Output definition

process.RAWSIMoutput = cms.OutputModule(
    "PoolOutputModule",
    splitLevel=cms.untracked.int32(0),
    eventAutoFlushCompressedSize=cms.untracked.int32(5242880),
    outputCommands=process.RAWSIMEventContent.outputCommands,
    fileName=cms.untracked.string("file:step1.root"),
    dataset=cms.untracked.PSet(
        filterName=cms.untracked.string(""), dataTier=cms.untracked.string("GEN-SIM")
    ),
    SelectEvents=cms.untracked.PSet(SelectEvents=cms.vstring("generation_step")),
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions = cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag

process.GlobalTag = GlobalTag(process.GlobalTag, "auto:startup", "")

process.generator = cms.EDFilter(
    "Pythia6GeneratorFilter",
    pythiaPylistVerbosity=cms.untracked.int32(0),
    filterEfficiency=cms.untracked.double(1.0),
    pythiaHepMCVerbosity=cms.untracked.bool(False),
    comEnergy=cms.double(8000.0),
    maxEventsToPrint=cms.untracked.int32(0),
    PythiaParameters=cms.PSet(
        pythiaUESettings=cms.vstring(
            "MSTU(21)=1     ! Check on possible errors during program execution",
            "MSTJ(22)=2     ! Decay those unstable particles",
            "PARJ(71)=10 .  ! for which ctau  10 mm",
            "MSTP(33)=0     ! no K factors in hard cross sections",
            "MSTP(2)=1      ! which order running alphaS",
            "MSTP(51)=10042 ! structure function chosen (external PDF CTEQ6L1)",
            "MSTP(52)=2     ! work with LHAPDF",
            "PARP(82)=1.921 ! pt cutoff for multiparton interactions",
            "PARP(89)=1800. ! sqrts for which PARP82 is set",
            "PARP(90)=0.227 ! Multiple interactions: rescaling power",
            "MSTP(95)=6     ! CR (color reconnection parameters)",
            "PARP(77)=1.016 ! CR",
            "PARP(78)=0.538 ! CR",
            "PARP(80)=0.1   ! Prob. colored parton from BBR",
            "PARP(83)=0.356 ! Multiple interactions: matter distribution parameter",
            "PARP(84)=0.651 ! Multiple interactions: matter distribution parameter",
            "PARP(62)=1.025 ! ISR cutoff",
            "MSTP(91)=1     ! Gaussian primordial kT",
            "PARP(93)=10.0  ! primordial kT-max",
            "MSTP(81)=21    ! multiple parton interactions 1 is Pythia default",
            "MSTP(82)=4     ! Defines the multi-parton model",
        ),
        processParameters=cms.vstring(
            "MSEL=0         ! User defined processes",
            "MSUB(11)=1     ! Min bias process",
            "MSUB(12)=1     ! Min bias process",
            "MSUB(13)=1     ! Min bias process",
            "MSUB(28)=1     ! Min bias process",
            "MSUB(53)=1     ! Min bias process",
            "MSUB(68)=1     ! Min bias process",
            "MSUB(92)=1     ! Min bias process, single diffractive",
            "MSUB(93)=1     ! Min bias process, single diffractive",
            "MSUB(94)=1     ! Min bias process, double diffractive",
            "MSUB(95)=1     ! Min bias process",
        ),
        parameterSets=cms.vstring("pythiaUESettings", "processParameters"),
    ),
)


# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(
    process.generation_step,
    process.genfiltersummary_step,
    process.simulation_step,
    process.endjob_step,
    process.RAWSIMoutput_step,
)
# filter all path with the production filter sequence
for path in process.paths:
    getattr(process, path)._seq = process.generator * getattr(process, path)._seq
