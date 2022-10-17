// Напишите программу, которая будет принимать на
// вход два числа и выводить, является ли второе число
// кратным первому. Если число 2 не кратно числу 1, то
// программа выводит остаток от деления.
// 34, 5 -> не кратно, остаток 4
// 16, 4 -> кратно


int Get(string message)
{
    Console.WriteLine(message);
    string numberAStr = Console.ReadLine();
    int numberA = Convert.ToInt32(numberAStr);
    return numberA;
}

int numberA = Get("Введите первое число:");
int numberB = Get("Введите второе число:");
int result = numberA % numberB;

if(result == 0)
{ 
    Console.WriteLine($"Число {numberA} является кратным числу {numberB}");
}
else
{ 
    Console.WriteLine($"Число {numberA} не является кратным числу {numberB}, остаток равен {result}");
}