def WriteFile(lines, path):
    f = open(path, "w")
    for el in lines:
        f.write(el+"\n")
    f.close()


def GetDiff(list1, list2):
    diff = list(set(list1) ^ set(list2))
    return diff


def GetDiffFile(path1, path2):
    with open(path1) as file1, open(path2) as file2:
        diff = GetDiff(file1, file2)
        WriteFile(diff, "write_files/diff.txt")
        return diff


def GetSame(file1, file2):
    same = list(set(file1).intersection(file2))
    return same


def GetSameFile(path1, path2):
    with open(path1) as file1, open(path2) as file2:
        same = GetSame((file1), (file2))
        WriteFile(same, "write_files/same.txt")
        return same


if __name__ == "__main__":
    path1 = 'read_files/file1.txt'
    path2 = 'read_files/file2.txt'
    print(GetSameFile(path1, path2))
    print(GetDiffFile(path1, path2))