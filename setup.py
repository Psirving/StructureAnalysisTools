from setuptools import setup, find_packages

setup(
    name="StructureAnalysisTools",
    packages=find_packages(include=["rnastruct", "rnastruct.*"]),
    package_dir={"": "./"},
    scripts=[
        "./rnastruct/ArcPlot.py",
        "./rnastruct/correlation_code.py",
        "./rnastruct/download_eclip.py",
        "./rnastruct/foldPK.py",
        "./rnastruct/get_from_genome.py",
        "./rnastruct/norm_correlation_code.py",
        "./rnastruct/pairmap_analysis.py",
    ],
    install_requires=[
        "pandas",
        "numpy",
        "matplotlib",
        "scipy",
        "requests",
        "pybedtools",
    ],
)
