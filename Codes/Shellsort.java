
public class ShellSort {
    public static void shellSort(int[] arr) {
        int n = arr.length;
        for (int gap = n/2; gap > 0; gap /= 2) {
            for (int i = gap; i < n; i++) {
                int temp = arr[i];
                int j = i;
                while (j >= gap && arr[j - gap] > temp) {
                    arr[j] = arr[j - gap];
                    j -= gap;
                }
                arr[j] = temp;
            }
        }
    }

    public static void printArray(int[] arr) {
        for (int x : arr) System.out.print(x + " ");
        System.out.println();
    }

    public static void main(String[] args) {
        int[] arr = {12, 34, 54, 2, 3};
        System.out.print("Исходный массив: ");
        printArray(arr);

        shellSort(arr);

        System.out.print("Отсортированный массив: ");
        printArray(arr);
    }
}
