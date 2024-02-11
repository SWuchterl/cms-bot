# CMS GIT Repositories automatic forward port map
# FORMAT:
# GIT_REPO_FWPORTS[repo][source-branch]=[destination-branch[:strategy]]
# e.g
# GIT_REPO_FWPORTS["cmssw"]["CMSSW_7_6_X"]=["CMSSW_7_6_ROOT64_X", "CMSSW_8_0_X:ours"]
from releases import CMSSW_DEVEL_BRANCH

GIT_REPO_FWPORTS = {"cmsdist": {}, "cmssw": {}}

# Added explicitly by Zygimantas Matonis
GIT_REPO_FWPORTS["cms-sw.github.io"] = {"code": ["master"]}

# Forward port master branch to latest dev branch
# Master branch is always forward ported to one branch.
GIT_REPO_FWPORTS["cmssw"]["master"] = [CMSSW_DEVEL_BRANCH]

GIT_REPO_FWPORTS["cmsdist"]["IB/CMSSW_7_1_X/stable"] = []
GIT_REPO_FWPORTS["cmsdist"]["IB/CMSSW_7_1_X/stable"].append("IB/CMSSW_7_1_X/pythia240")
GIT_REPO_FWPORTS["cmssw"]["CMSSW_7_1_X"] = []
GIT_REPO_FWPORTS["cmssw"]["CMSSW_7_1_X"].append("CMSSW_7_1_PYTHIA240_X")

GIT_REPO_FWPORTS["cmsdist"]["IB/CMSSW_9_1_X/gcc530"] = []
GIT_REPO_FWPORTS["cmsdist"]["IB/CMSSW_9_1_X/gcc530"].append("IB/CMSSW_9_1_X/gcc630")

GIT_REPO_FWPORTS["cmsdist"]["IB/CMSSW_9_2_X/gcc530"] = []
GIT_REPO_FWPORTS["cmsdist"]["IB/CMSSW_9_2_X/gcc530"].append("IB/CMSSW_9_2_X/gcc630")

# Added explicitly by Shahzad MUZAFFAR
GIT_REPO_FWPORTS["cmssw"]["CMSSW_9_4_X"] = []
GIT_REPO_FWPORTS["cmssw"]["CMSSW_9_4_X"].append("CMSSW_9_4_MAOD_X")
GIT_REPO_FWPORTS["cmssw"]["CMSSW_9_4_X"].append("CMSSW_9_4_AN_X")

# Automatically added
GIT_REPO_FWPORTS["cmsdist"]["IB/CMSSW_10_1_X/gcc630"] = []
GIT_REPO_FWPORTS["cmsdist"]["IB/CMSSW_10_1_X/gcc630"].append("IB/CMSSW_10_1_X/gcc700")

# Automatically added
GIT_REPO_FWPORTS["cmsdist"]["IB/CMSSW_11_0_X/master"] = []
GIT_REPO_FWPORTS["cmsdist"]["IB/CMSSW_11_0_X/master"].append("IB/CMSSW_11_0_X/cc8")

# Automatically added
GIT_REPO_FWPORTS["cmsdist"]["IB/CMSSW_11_1_X/master"] = []
GIT_REPO_FWPORTS["cmsdist"]["IB/CMSSW_11_1_X/master"].append("IB/CMSSW_11_1_X/cc8")

# Automatically added
GIT_REPO_FWPORTS["cmsdist"]["IB/CMSSW_11_2_X/master"] = []
GIT_REPO_FWPORTS["cmsdist"]["IB/CMSSW_11_2_X/master"].append("IB/CMSSW_11_2_X/cc8")

# Automatically added
GIT_REPO_FWPORTS["cmsdist"]["IB/CMSSW_11_3_X/master"] = []
GIT_REPO_FWPORTS["cmsdist"]["IB/CMSSW_11_3_X/master"].append("IB/CMSSW_11_3_X/cc8")

# Automatically added
GIT_REPO_FWPORTS["cmsdist"]["IB/CMSSW_12_0_X/master"] = []
GIT_REPO_FWPORTS["cmsdist"]["IB/CMSSW_12_0_X/master"].append("IB/CMSSW_12_0_X/cc8")

# Automatically added
GIT_REPO_FWPORTS["cmsdist"]["IB/CMSSW_12_1_X/master"] = []
GIT_REPO_FWPORTS["cmsdist"]["IB/CMSSW_12_1_X/master"].append("IB/CMSSW_12_1_X/cc8")

# Automatically added
GIT_REPO_FWPORTS["cmsdist"]["IB/CMSSW_12_2_X/master"] = []
GIT_REPO_FWPORTS["cmsdist"]["IB/CMSSW_12_2_X/master"].append("IB/CMSSW_12_2_X/cc8")

# Automatically added
GIT_REPO_FWPORTS["cmsdist"]["IB/CMSSW_12_5_X/master"] = []
GIT_REPO_FWPORTS["cmsdist"]["IB/CMSSW_12_5_X/master"].append("IB/CMSSW_12_5_X/g11")

# Automatically added
GIT_REPO_FWPORTS["cmsdist"]["IB/CMSSW_12_6_X/master"] = []
GIT_REPO_FWPORTS["cmsdist"]["IB/CMSSW_12_6_X/master"].append("IB/CMSSW_12_6_X/g11")

# Automatically added
GIT_REPO_FWPORTS["cmsdist"]["IB/CMSSW_13_0_X/master"] = []
GIT_REPO_FWPORTS["cmsdist"]["IB/CMSSW_13_0_X/master"].append("IB/CMSSW_13_0_X/cs9")

# Automatically added
GIT_REPO_FWPORTS["cmsdist"]["IB/CMSSW_13_1_X/master"] = []
GIT_REPO_FWPORTS["cmsdist"]["IB/CMSSW_13_1_X/master"].append("IB/CMSSW_13_1_X/cs9")

# Automatically added
GIT_REPO_FWPORTS["cmsdist"]["IB/CMSSW_13_2_X/master"] = []
GIT_REPO_FWPORTS["cmsdist"]["IB/CMSSW_13_2_X/master"].append("IB/CMSSW_13_2_X/cs9")

# Automatically added
GIT_REPO_FWPORTS["cmsdist"]["IB/CMSSW_13_3_X/master"] = []
GIT_REPO_FWPORTS["cmsdist"]["IB/CMSSW_13_3_X/master"].append("IB/CMSSW_13_3_X/cs9")

# Automatically added
GIT_REPO_FWPORTS["cmssw"]["CMSSW_14_0_X"] = []
GIT_REPO_FWPORTS["cmssw"]["CMSSW_14_0_X"].append("CMSSW_14_0_DEVEL_X")
GIT_REPO_FWPORTS["cmsdist"]["IB/CMSSW_14_0_X/master"] = []
GIT_REPO_FWPORTS["cmsdist"]["IB/CMSSW_14_0_X/master"].append("IB/CMSSW_14_0_X/root626")
GIT_REPO_FWPORTS["cmsdist"]["IB/CMSSW_14_0_X/master"].append("IB/CMSSW_14_0_X/root628")
GIT_REPO_FWPORTS["cmsdist"]["IB/CMSSW_14_0_X/master"].append("IB/CMSSW_14_0_X/root630")
GIT_REPO_FWPORTS["cmsdist"]["IB/CMSSW_14_0_X/master"].append("IB/CMSSW_14_0_X/rootmaster")
GIT_REPO_FWPORTS["cmsdist"]["IB/CMSSW_14_0_X/master"].append("IB/CMSSW_14_0_X/cs9")
GIT_REPO_FWPORTS["cmsdist"]["IB/CMSSW_14_0_X/master"].append("IB/CMSSW_14_0_X/g4")
GIT_REPO_FWPORTS["cmsdist"]["IB/CMSSW_14_0_X/master"].append("IB/CMSSW_14_0_X/cudart")
GIT_REPO_FWPORTS["cmsdist"]["IB/CMSSW_14_0_X/master"].append("IB/CMSSW_14_0_X/g13")
GIT_REPO_FWPORTS["cmsdist"]["IB/CMSSW_14_0_X/rootmaster"] = ["IB/CMSSW_14_0_X/rootmodule"]

# Automatically added
GIT_REPO_FWPORTS["cmssw"]["CMSSW_14_1_X"] = []
GIT_REPO_FWPORTS["cmssw"]["CMSSW_14_1_X"].append("CMSSW_14_1_DEVEL_X")
GIT_REPO_FWPORTS["cmsdist"]["IB/CMSSW_14_1_X/master"] = []
GIT_REPO_FWPORTS["cmsdist"]["IB/CMSSW_14_1_X/master"].append("IB/CMSSW_14_1_X/root626")
GIT_REPO_FWPORTS["cmsdist"]["IB/CMSSW_14_1_X/master"].append("IB/CMSSW_14_1_X/root628")
GIT_REPO_FWPORTS["cmsdist"]["IB/CMSSW_14_1_X/master"].append("IB/CMSSW_14_1_X/root630")
GIT_REPO_FWPORTS["cmsdist"]["IB/CMSSW_14_1_X/master"].append("IB/CMSSW_14_1_X/rootmaster")
GIT_REPO_FWPORTS["cmsdist"]["IB/CMSSW_14_1_X/master"].append("IB/CMSSW_14_1_X/cs9")
GIT_REPO_FWPORTS["cmsdist"]["IB/CMSSW_14_1_X/master"].append("IB/CMSSW_14_1_X/g4")
GIT_REPO_FWPORTS["cmsdist"]["IB/CMSSW_14_1_X/master"].append("IB/CMSSW_14_1_X/cudart")
GIT_REPO_FWPORTS["cmsdist"]["IB/CMSSW_14_1_X/master"].append("IB/CMSSW_14_1_X/g13")
GIT_REPO_FWPORTS["cmsdist"]["IB/CMSSW_14_1_X/master"].append("IB/CMSSW_14_1_X/tf")
GIT_REPO_FWPORTS["cmsdist"]["IB/CMSSW_14_1_X/rootmaster"] = ["IB/CMSSW_14_1_X/rootmodule"]
