# Timer Polling (Create a us Function)

In this lab, we use a time polling mode with TIMER6 of the stm32f4. In this scenario, we like to create a precise micro second function, so first we need to configure the clock as shown in the image belwo



![stm32F407VGT6](https://github.com/Theara-Seng/stm32_lab/blob/main/tim_polling_us/image/clock.png)


From the image above, we see that the clock configure is 168MHz and the APB2 Peripheral clock is 84MHz, so in order to create a 1 us we need to use a prescaler of 168-1 so that we get 


$$ delay = \dfrac{Peripheral clock}{prescaler+1}= \dfrac{84MHz}{167+1} = 1Mhz = 1 micro second $$ 

So the counter period when it count up to 65535 or 0xFFFF, it will overflow to 0.


We need to configure the timer6 and prescale clock as shown in the image below


![stm32F407VGT6](https://github.com/Theara-Seng/stm32_lab/blob/main/tim_polling_us/image/configure.png)


## Programming


First we need to call a timer6 base start from HAL library in the main function

```sh
HAL_StatusTypeDef HAL_TIM_Base_Start(TIM_HandleTypeDef *htim)
```

So, we can write 

```sh
 HAL_TIM_Base_Start(&htim6);
 ```
 
 Then we can create a Delay function count from 1us up to any second
 
 ```sh 
void delay(uint16_t delays){
	for (uint16_t i =1; i<=delays; i++){
		uint16_t start = TIM6->CNT;
		while((TIM6->CNT - start)< 1);
	}
}
```

After that we can test this function to toggle a PIN 1 of GPIOA as shown in the code here


```sh
HAL_GPIO_TogglePin(GPIOA, GPIO_PIN_1);
delay(1000);
 ```
## Result

We can see the GPIOA with PIN 1 is toggle every one millis second as shown in the image below

![stm32F407VGT6](https://github.com/Theara-Seng/stm32_lab/blob/main/tim_polling_us/image/1ms.png)
