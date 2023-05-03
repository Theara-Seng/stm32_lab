# Button Polling

In this project we will using button polling concept that when the button is pressed the all the led pins will turn on and if release, the led pins are turn off

we configure the same concept as the led as last lesson but we need to change the button pin to GPIO_Input since we use the polling concept, The button is active high so when the button is high
the led will turn off


![stm32F407VGT6](https://github.com/Theara-Seng/stm32_lab/blob/main/button/image/input_gpio.png)


## Coding 


```sh
if (HAL_GPIO_ReadPin(GPIOA, GPIO_PIN_0)==GPIO_PIN_SET){
    	HAL_GPIO_WritePin(GPIOD, GPIO_PIN_12, GPIO_PIN_SET);
    	HAL_GPIO_WritePin(GPIOD, GPIO_PIN_13, GPIO_PIN_SET);
    	HAL_GPIO_WritePin(GPIOD, GPIO_PIN_14, GPIO_PIN_SET);
    	HAL_GPIO_WritePin(GPIOD, GPIO_PIN_15, GPIO_PIN_SET);

}else{
      HAL_GPIO_WritePin(GPIOD, GPIO_PIN_12, GPIO_PIN_RESET);
      HAL_GPIO_WritePin(GPIOD, GPIO_PIN_13, GPIO_PIN_RESET);
      HAL_GPIO_WritePin(GPIOD, GPIO_PIN_14, GPIO_PIN_RESET);
      HAL_GPIO_WritePin(GPIOD, GPIO_PIN_15, GPIO_PIN_RESET);
}
```

In this code, we write a code that read the GPIOA pin, if the pin is set, we turn on all the led, else all the led will turn off

After click on the resume when we press the button, we see all the led will turn on as shown in the image below


![stm32F407VGT6](https://github.com/Theara-Seng/stm32_lab/blob/main/button/image/button_press.jpg)
