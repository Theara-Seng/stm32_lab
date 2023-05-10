# TIMER Interrupt 

In this Lab, we want to create a delay of 1 second using timer interrupt mode.

Before start the program, we need to understand some basic timer:

* Basic timer is a free-running counter, which counts from 0 up to the value specified in the period field in the **TIM_Base_InitTypeDef** initialization structure, which can assume the maximum value of 0xFFFF (for 32 bit timer)

* The counting frequency depends on the speed of the bus where the timer is connected, and it can be lowered up to 65536 times by setting the Prescaler register in the initialization structure;

* When the timer reaches the Period value it overflows, and the Update Event (UEV) flag is set then the timer automatically restarts counting again from the initial value

The **Period** and **Prescaler** Registers determine the time frequency, that is how long does it takes to overflow, according to this formula

$$ UpdateEvent = \dfrac{Timer_clock}{(Prescaler+1)(Period+1)} $$

So If we want to create a 1 second delay, we need to configure the **Clock**, **Prescaler**, **Period**. We choose the **clock** of 168MHz and the **period** is 999 and the **prescaler** is 16799, then we get:

$$ delay = \dfrac{168\times10^{6}}{(9999+1)(16799+1)} = 1HZ = 1 second$$

So first we can go to configure the timer, In this can I chose the timer10 and configure the period and prescaler as shown in the image below

![stm32F407VGT6](https://github.com/Theara-Seng/stm32_lab/blob/main/tim_interrupt/image/configure.png)

Then we need also choose the NVIC to enable timer interrupt as shown in the image below

![stm32F407VGT6](https://github.com/Theara-Seng/stm32_lab/blob/main/tim_interrupt/image/nvic.png)

After that in the clock configuration we need to set it 168000000 as shown here

![stm32F407VGT6](https://github.com/Theara-Seng/stm32_lab/blob/main/tim_interrupt/image/clock.png)


After that we can go to the main.c 


## Programming

First we need to call the HAL library interrupt which is 

```sh
HAL_StatusTypeDef HAL_TIM_Base_Start_IT(TIM_HandleTypeDef *htim);
```

By using Timer10, then we write in the main funciont in the **USER Begin Code 2**

```sh 
  HAL_TIM_Base_Start_IT(&htim10);
```

After that we can call a call back function in the **USER Begin Code 4**

```sh
void HAL_TIM_PeriodElapsedCallback(TIM_HandleTypeDef *htim)
```

```sh
void HAL_TIM_PeriodElapsedCallback(TIM_HandleTypeDef *htim)
{
	if (htim == &htim10){
		HAL_GPIO_TogglePin(GPIOD, GPIO_PIN_12);
	}
}
```

# Result 

Then we can see the PIN 12 of Port D is blinking every one second as shown in the graph here


![stm32F407VGT6](https://github.com/Theara-Seng/stm32_lab/blob/main/tim_interrupt/image/second_delay.png)
