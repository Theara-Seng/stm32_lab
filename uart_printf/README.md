# printf function (USART2)

In this case, we want to create a printf function using USART2 which can printing all the data without using the 

```sh
HAL_StatusTypeDef HAL_UART_Transmit(UART_HandleTypeDef *huart, uint8_t *pData, uint16_t Size, uint32_t Timeout);
```
In order to do that we need to configure the USART2 also as shown in th image below


![stm32F407VGT6](https://github.com/Theara-Seng/stm32_lab/blob/main/uart_printf/image/usart2.png)


## Coding 

We need to write a function which can use with printf as shown in the code below
```sh
int _write(int file, char* p, int len){
	HAL_UART_Transmit(&huart2, p, len, 10);
	return len;

}
``` 

with this function, you then can use printf to print as **C program** which you dont have to transmit data, just using this function it will transmit data directly.

### Example 

in the while loop you can print something like this
```sh
 printf("Hello World->");
HAL_Delay(1000);
printf("integer = %d->",msg);
HAL_Delay(1000);
```

### Noted

However you can not print floating number until you configue the floating value as shown in the image below


![stm32F407VGT6](https://github.com/Theara-Seng/stm32_lab/blob/main/uart_printf/image/printf.png)

After that you can print the floating number without error

```sh
    printf("Hello World->");
    HAL_Delay(1000);
    printf("integer = %d->",msg);
    HAL_Delay(1000);
    printf("float= %f\n", f);
    HAL_Delay(1000);
```

### Result 

![stm32F407VGT6](https://github.com/Theara-Seng/stm32_lab/blob/main/uart_printf/image/data.png)
