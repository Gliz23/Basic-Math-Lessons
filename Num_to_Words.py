num_to_words={1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five', 6 : 'six', 7 : 'seven',
8 : 'eight', 9 : 'nine', 10 : 'ten', 11 : 'eleven', 12 : 'twelve', 13 : 'thirteen',
14 : 'fourteen', 15 : 'fifteen',16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
19 : 'nineteen', 20 : 'twenty', 30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty',
70 : 'seventy', 80 : 'eighty', 90 : 'ninety', 100 : 'hundred', 200: 'two-hundred',
300: 'three-hundred', 400: 'four-hundred', 500: 'five-hundred', 600: 'six-hundred', 
700: 'seven-hundred', 800: 'eight-hundred', 900: 'nine-hundred', 1000: 'one-thousand',
2000: 'two-thousand', 3000: 'three-thousand', 4000: 'four-thousand', 5000: 'five-thousand',
6000: 'six-thousand', 7000: 'seven-thousand', 8000: 'eight-thousand', 9000: 'nine-thousand',
10000: 'ten-thousand', 20000: 'twenty thousand', 30000: 'thirty thousand', 40000: 'forty thousand', 
50000: 'fifty thousand', 60000: 'sixty thousand', 70000: 'seventy thousand', 80000: 'eighty thousand', 
90000: 'ninety thousand', 100000: 'one hundred thousand', 200000: 'two hundred thousand', 300000: 
'three hundred thousand', 400000: 'four hundred thousand', 500000: 'five hundred thousand', 
600000: 'six hundred thousand', 700000: 'seven hundred thousand', 800000: 'eight hundred thousand', 
900000: 'nine hundred thousand', 1000000: 'one million', 2000000: 'two million', 3000000: 'three million', 
4000000: 'four million', 5000000: 'five million', 6000000: 'six million', 7000000: 'seven million', 8000000: 
'eight million', 9000000: 'nine million', 10000000: 'ten million', 20000000: 'twenty million', 30000000: 
'thirty million', 40000000: 'forty million', 50000000: 'fifty million', 60000000: 'sixty million', 
70000000: 'seventy million', 80000000: 'eighty million', 90000000: 'ninety million', 100000000: 'one hundred million',
200000000: 'two hundred million', 300000000: 'three hundred million', 400000000: 'four hundred million', 
500000000: 'five hundred million', 600000000: 'six hundred million', 700000000: 'seven hundred million', 
800000000: 'eight hundred million',900000000: 'nine hundred million', 1000000000: 'one billion'}

num = int(input("Enter a number: "))

if num<= 1000000000:
    if num in num_to_words:
        words = num_to_words.get(num)
        print(words)
    else:
        if 0 < num < 100:
            ones = num%10
            ones = num_to_words.get(ones)
            tens = num//10
            tens = tens * 10
            tens = num_to_words.get(tens)
            tens_in_words = f"{tens} {ones}"
            print(tens_in_words)
        elif 101 < num < 1000:
            ones = num%10
            ones = num_to_words.get(ones)
            tens = ((num//10) % 10) * 10
            tens = num_to_words.get(tens)
            hunds = num // 100
            hunds = hunds * 100
            hunds = num_to_words.get(hunds)
            hunds_in_words = f"{hunds} {tens} {ones}"
            print(hunds_in_words)
else:
    print(num)

