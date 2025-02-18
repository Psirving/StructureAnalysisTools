from setuptools import setup, find_packages

setup(
    name="StructureAnalysisTools",
    packages=find_packages(
        include=["StructureAnalysisTools", "StructureAnalysisTools.*"]
    ),
    package_dir={"StructureAnalysisTools": "./"},
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
