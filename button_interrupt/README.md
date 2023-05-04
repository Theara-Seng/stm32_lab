# Button Intrrupt

We will use the **User Button** on the stm32 as the external interrupt. THe User Button is connected to the the pin PA0, so we need to configue it as **GPIO_EXTI0**



![stm32F407VGT6](https://github.com/Theara-Seng/stm32_lab/blob/main/button_interrupt/image/interrupt.png)


And we also need to activate the NVIC and click on the EXTI_LINE0_INTERRUPT as shown in the image below


![stm32F407VGT6](https://github.com/Theara-Seng/stm32_lab/blob/main/button_interrupt/image/nvic.png)


When we generate the code we can see the interrupt vecotor in the file **stm32f4xx_it.c** as shown in the image below

![stm32F407VGT6](https://github.com/Theara-Seng/stm32_lab/blob/main/button_interrupt/image/IRQ.png)


## Programming

Using the interrupt, we do not write the code in the while loop, so we will write the code below the declaration of the pin or finding the comment **/* USER CODE BEGIN 4 */**

```sh
void HAL_GPIO_EXTI_Callback(uint16_t GPIO_Pin){

	if (GPIO_Pin == GPIO_PIN_0){
		HAL_GPIO_TogglePin(GPIOD, GPIO_PIN_12);
		HAL_GPIO_TogglePin(GPIOD, GPIO_PIN_13);
		HAL_GPIO_TogglePin(GPIOD, GPIO_PIN_14);
		HAL_GPIO_TogglePin(GPIOD, GPIO_PIN_15);
	}
}
```

The code above when one button is pressed, if the state is low, it will change to High. Then pressing one more time, it will change the state to Low again.
