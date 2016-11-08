public static int digitCount(int number, int digit) {

	int count = 0;
	int remainder = 0;
	while (number > 0 ) {
		remainder = number % 10;
		if (remainder == digit) {
			count = count + 1;
		}
		number = number/10;
	}
	return count;
}


public static void main(string[] args) {
	int num = 333;
	int digit = 3;
	int result = digitCount(num, digit);

	system.out.println(result);
}