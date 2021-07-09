import inspect
import os

capitalCamelCase = lambda path: "".join(
    [i.capitalize() for i in os.path.basename(path).split(".")[0].split("_")]
)


def genCassetteName():
    currentTest = os.environ.get("PYTEST_CURRENT_TEST")
    testDir, testName = currentTest.split("::")
    testDir = capitalCamelCase(os.path.basename(testDir))
    testName = testName.split(" ")[0]
    return f"{testDir}.{testName}"
