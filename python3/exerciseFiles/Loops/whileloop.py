def main():
    secret = 'secret word'
    pw = ''
    auth = False
    count = 0
    max_attempt = 5
    while pw != secret:
        # increment count
        count += 1
        # break will break all the way out of the loop
        if count > max_attempt:
            break
        # this tests the continue again
        if count == 3:
            continue
        pw = input('{count}: Whats the secret word?: ')

    else:  # only executes if while returns true

        auth = True
    print("authorized" if auth else "calling the FBI ..")


main()
