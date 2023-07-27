import java.util.Scanner;


public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);


        System.out.println("Please enter numbers seperated by a comma");

        String values = scanner.nextLine();
        String[] yourArray = values.split(",");
        int[] array = new int[yourArray.length];

        for (int i = 0; i < yourArray.length; i++) {
            array[i] = Integer.parseInt(yourArray[i]);
        }

        System.out.println("Enter the key you want to search for:");
        int key = scanner.nextInt();

        int index = linearSearch(array, key);


        if (index != -1) {
            System.out.println("Key found at index: " + index);
        } else {
            System.out.println(("Key not found"));
        }
    }

    private static int linearSearch(int[] arrayExample, int keyExample) {
        for(int i =0; i < arrayExample.length; i++) {
            if(arrayExample[i]== keyExample) {
                return i;
            }
        }
        return -1;
    }







}

