def determinePrecedence(semverHigh, semverLow):
    # validate
    # no validation - input is assumed to be valid semver strings that MIGHT include prerelease versioning
    #                 but NO build metadata

    if semverHigh == semverLow:
        return True

    # Extract parts using string manipulation
    # split into [version-core, pre-release] OR [version-core] parts
    semverHighVersionCorePreRelease = semverHigh.split("-", 1)
    semverLowVersionCorePreRelease = semverLow.split("-", 1)

    # split into [major, minor, patch] parts
    semverHighParts = semverHighVersionCorePreRelease[0].split(".")
    semverLowParts = semverLowVersionCorePreRelease[0].split(".")

    # compare major
    if int(semverHighParts[0]) > int(semverLowParts[0]):
        return True
    elif int(semverHighParts[0]) < int(semverLowParts[0]):
        return False
    # major is equal, therefore compare minor
    elif int(semverHighParts[1]) > int(semverLowParts[1]):
        return True
    elif int(semverHighParts[1]) < int(semverLowParts[1]):
        return False
    # major and minor are equal, therefore compare patch
    elif int(semverHighParts[2]) > int(semverLowParts[2]):
        return True
    elif int(semverHighParts[2]) < int(semverLowParts[2]):
        return False
    # version-core is equal - compare pre-release
    # if semver_high has a pre-release and semver_low does not, semver_low is more recent
    elif len(semverHighVersionCorePreRelease) == 2 and len(semverLowVersionCorePreRelease) == 1:
        return False
    # else, compare the pre-release values

    return True

