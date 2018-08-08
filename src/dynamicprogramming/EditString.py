
def edit_string_recursive(strA, strB, m, n):

    if m == 0:
        return n

    if n == 0:
        return m

    if strA[m-1] == strB[n-1]:
        return edit_string_recursive(strA, strB, m-1, n-1)

    return 1 + min(edit_string_recursive(strA, strB, m, n-1),
                   edit_string_recursive(strA, strB, m-1, n),
                   edit_string_recursive(strA, strB, m-1, n-1))


def dynamic_approch_of_edit_string(a, b, m, n):
    dp = [[0 for k in range(n+1)] for x in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                dp[i][j] = j    # Min. operations = j

            # If second string is empty, only option is to
            # remove all characters of second string
            elif j == 0:
                dp[i][j] = i    # Min. operations = i

            # If last characters are same, ignore last char
            # and recur for remaining string
            elif a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1]

            # If last character are different, consider all
            # possibilities and find minimum
            else:
                dp[i][j] = 1 + min(dp[i][j-1],        # Insert
                                   dp[i-1][j],        # Remove
                                   dp[i-1][j-1])

    return dp[m][n]


if __name__ == '__main__':
    a = "Gopi is very good boyasdmnasduasdimasnjdaiusudhiausduinkajncsuasdnaiscuiascaslckascnlkaslkckanscaclkanslnascasklcnlkascuascnlansclkascnksjdvbiuakdsvaksvnamvnasdvbsdvlDSFOASFl;asfnldfjdsfksdkjfskdf"
    b = "fridayacasdafhasdkfalkjfdhas,dncalksdjghalsdkgjhanckasdghaisgjnaksvnapsgusduigausdasdnvasdghasdghaklsdglas;dghaskjghasigdkas,dfmnkasgiaslkdjgaisdjgknsakdvuiiasdkgnapsiughaksdgnlakscamciosiofoiagdavwioegsmdkidvdvmlascmcakscmaksvlsidhbosdvnlsdivojosidvlsdkvmsdvio"

    #print(edit_string_recursive(a, b, len(a), len(b)))
    print(dynamic_approch_of_edit_string(a, b, len(a), len(b)))
