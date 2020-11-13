import re


# https://docs.python.org/3/howto/regex.html
def determinePrecedence(semverHigh, semverLow):
    # validate
    # no validation - input is assumed to be valid semver strings that MIGHT include prerelease versioning
    #                 but NO build metadata

    if semverHigh == semverLow:
        return True

    # Extract parts using regular expression
    #           (major) .(minor) .(patch) OPTIONAL(-) OPTIONAL(rest of string)
    pattern = '^([\d]+)\.([\d]+)\.([\d]+)(?:-(.+))?$'
    semverHighParts = re.search(pattern, semverHigh)
    semverLowParts = re.search(pattern, semverLow)

    # compare major
    if int(semverHighParts.group(1)) > int(semverLowParts.group(1)):
        return True
    elif int(semverHighParts.group(1)) < int(semverLowParts.group(1)):
        return False
    # major is equal, therefore compare minor
    elif int(semverHighParts.group(2)) > int(semverLowParts.group(2)):
        return True
    elif int(semverHighParts.group(2)) < int(semverLowParts.group(2)):
        return False
    # major and minor are equal, therefore compare patch
    elif int(semverHighParts.group(3)) > int(semverLowParts.group(3)):
        return True
    elif int(semverHighParts.group(3)) < int(semverLowParts.group(3)):
        return False

    # version-core is equal - compare pre-release
    # if semver_high has a pre-release and semver_low does not, semver_low is more recent
    if semverHighParts.group(4) is not None and semverLowParts.group(4) is None:
        return False
    # else, compare the pre-release values

    return True
