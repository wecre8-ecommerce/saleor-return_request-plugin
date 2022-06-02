from setuptools import setup

setup(
    name="return-request",
    version="0.1.0",
    packages=["return_request"],
    package_dir={"return_request": "return_request"},
    description="Return request plugin",
    entry_points={
        "saleor.plugins": ["return_request = return_request.plugin:ReturnRequestPlugin"],
    },
)
