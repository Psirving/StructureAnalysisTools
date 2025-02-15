from setuptools import setup, find_packages

setup(
    name="StructureAnalysisTools",
    scripts=[
        "ArcPlot.py",
        "correlation_code.py",
        "download_eclip.py",
        "foldPK.py",
        "get_from_genome.py",
        "norm_correlation_code.py",
        "pairmap_analysis.py",
    ],
    packages=find_packages(),
)
