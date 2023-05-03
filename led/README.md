# LED BLINK

## Pin and Clock configuration

After create a new project and giving the project name, then we will go to the **Pinout & Configuration**

![stm32F407VGT6](https://github.com/Theara-Seng/stm32_lab/blob/main/led/image/pin_out.png)



There are 4 LED Pins in the stm32F407VGT6, so 4 of them are configured as the GPIO OUTPUT

![stm32F407VGT6](https://github.com/Theara-Seng/stm32_lab/blob/main/led/image/output_pin.png)

And in the clock configuration, choosing the desire clock on your own

![stm32F407VGT6](https://github.com/Theara-Seng/stm32_lab/blob/main/led/image/clock_selection.png)


Then go to **Led->Core->main.c**

![stm32F407VGT6](https://github.com/Theara-Seng/stm32_lab/blob/main/led/image/main.png)

and select yes for this case

![stm32F407VGT6](https://github.com/Theara-Seng/stm32_lab/blob/main/led/image/yes_selection.png)

After that you will go to the C/C++ program section 

## Coding

In the **While (1)**, we will write a program which blink the 4 led pin every 1 second

```sh
HAL_GPIO_WritePin(GPIOD, GPIO_PIN_12, GPIO_PIN_SET);
HAL_GPIO_WritePin(GPIOD, GPIO_PIN_13, GPIO_PIN_SET);
HAL_GPIO_WritePin(GPIOD, GPIO_PIN_14, GPIO_PIN_SET);
HAL_GPIO_WritePin(GPIOD, GPIO_PIN_15, GPIO_PIN_SET);

HAL_Delay(1000);

HAL_GPIO_WritePin(GPIOD, GPIO_PIN_12, GPIO_PIN_RESET);
HAL_GPIO_WritePin(GPIOD, GPIO_PIN_13, GPIO_PIN_RESET);
HAL_GPIO_WritePin(GPIOD, GPIO_PIN_14, GPIO_PIN_RESET);
HAL_GPIO_WritePin(GPIOD, GPIO_PIN_15, GPIO_PIN_RESET);

HAL_Delay(1000);
```
We write the pin (12,13,14 and 15) of port D to high using the **GPIO_PIN_SET** for 1 second and after that we using the **GPIO_PIN_RESET** to get them turn off for 1 second

*** Using TogglePin 

We also can use the togglePin to blink the led every 1 second with the code below

```sh
  HAL_GPIO_TogglePin(GPIOD, GPIO_PIN_12);
  HAL_GPIO_TogglePin(GPIOD, GPIO_PIN_13);
  HAL_GPIO_TogglePin(GPIOD, GPIO_PIN_14);
  HAL_GPIO_TogglePin(GPIOD, GPIO_PIN_15);
  HAL_Delay(1000);
```

After writing the code, we need to build the project and if there is no error message, then we can click on the debug as shown in the image below

![stm32F407VGT6](https://github.com/Theara-Seng/stm32_lab/blob/main/led/image/build.png)


After that we need to click on the resume

![stm32F407VGT6](https://github.com/Theara-Seng/stm32_lab/blob/main/led/image/resume.png)


After that we can see the led light up for 1 second 

![stm32F407VGT6](https://github.com/Theara-Seng/stm32_lab/blob/main/led/image/high.jpg)

and then turn off for 1 second 

![stm32F407VGT6](https://github.com/Theara-Seng/stm32_lab/blob/main/led/image/low.jpg)
