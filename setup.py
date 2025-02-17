from setuptools import setup

setup(
    name="StructureAnalysisTools",
    packages=["StructureAnalysisTools"],
    package_dir={"StructureAnalysisTools": "./"},
    py_modules=[
        "StructureAnalysisTools.ArcPlot",
        "StructureAnalysisTools.correlation_code",
        "StructureAnalysisTools.download_eclip",
        "StructureAnalysisTools.foldPK",
        "StructureAnalysisTools.get_from_genome",
        "StructureAnalysisTools.mean_reactivity_stdev",
        "StructureAnalysisTools.norm_correlation_code",
        "StructureAnalysisTools.pairmap_analysis",
        "StructureAnalysisTools.ReactivityProfile",
        "StructureAnalysisTools.RNAStructureObjects",
    ],
    scripts=[
        "./StructureAnalysisTools/ArcPlot.py",
        "./StructureAnalysisTools/correlation_code.py",
        "./StructureAnalysisTools/download_eclip.py",
        "./StructureAnalysisTools/foldPK.py",
        "./StructureAnalysisTools/get_from_genome.py",
        "./StructureAnalysisTools/norm_correlation_code.py",
        "./StructureAnalysisTools/pairmap_analysis.py",
    ],
)
