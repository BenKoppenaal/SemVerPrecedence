
# official code style - https://www.python.org/dev/peps/pep-0008/
# Python Developer's Guide - https://devguide.python.org/
# semver syntax - https://semver.org/#backusnaur-form-grammar-for-valid-semver-versions

def determinePrecedence(semver_high, semver_low):
    # validate
    # no validation - input is assumed to be valid semver strings potentially appended with prerelease versioning

    # edge case - if both semver versions are equal
    if semver_high == semver_low:
        return True

    # split into [version-core, pre-release] OR [version-core] parts
    # TODO: think of a better variable name
    semver_high_pre_release = semver_high.split("-", 1)
    semver_low_pre_release = semver_low.split("-", 1)

    # split into [major, minor, patch] parts
    semver_high_parts = semver_high_pre_release[0].split(".")
    semver_low_parts = semver_low_pre_release[0].split(".")

    # compare major
    if int(semver_high_parts[0]) > int(semver_low_parts[0]):
        return True
    if int(semver_high_parts[0]) < int(semver_low_parts[0]):
        return False

    # major is equal, therefore compare minor
    elif int(semver_high_parts[1]) > int(semver_low_parts[1]):
        return True
    elif int(semver_high_parts[1]) < int(semver_low_parts[1]):
        return False

    # major and minor are equal, therefore compare patch
    elif int(semver_high_parts[2]) > int(semver_low_parts[2]):
        return True
    elif int(semver_high_parts[2]) < int(semver_low_parts[2]):
        return False

    # compare pre-release

    # default case occurs when both semver strings are equal.
    # TODO: also put equal string at the top?
    return True


if __name__ == '__main__':
    if determinePrecedence("0.1.2-beta", "3.14.0"):
        print("Higher version")
    else:
        print("Lower version")
