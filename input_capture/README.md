# Input Capture Mode (Timer)

We use input capture to measure the frequency of a device which is generated from the device.

The **Input Capture Mode** offered by general purpose and advanced timers allows to compute the frequency of external singals applied to each one of the 4 channels that these timers provide. 
And the capture is perfored indepdently for each channel.


![stm32F407VGT6](https://github.com/Theara-Seng/stm32_lab/blob/main/input_capture/image/capture_process.png)


The image above shows how the caputure process works. **TIMx** is a timer, configured to workd given **TIMx_CLK** clock frequency. This means that it increment the **TIMx_CNT** register up to the 
period value every $\dfrac{1}{TIMx\_{CLK}}$ second. 

Suppose that we apply a square wave signal to one of the timer channls, and supposing that we configure the timer to trigger at every rising edge of the input signal, we have that the **TIMx_CCRx**
register will be updated with the content of the **TIMx_CNT** register at every detected transition. When this happens, the timer will generate a corresponding interrupt or a DMA request allowing to keep track of the counter value.

Example if we capture the first rising edge is 0x00ff and then the second rising edge is 0xffff then the different is 0xffff-0x00fff is the counting value **TIM->CNT**

By using th formular 

$$ period = \dfrac{TIMx_{CLK}}{(prescaler+1)(counter+1)} $$

The counter is the different between two rising edge value, Then we can find the the frequency of the device by formula $ Capture = CNT1 - CNT0 $

However, there are different scenario that the first capture is 0xFFFF and the second capture is 0x00FF so we cannot capture this case 

![stm32F407VGT6](https://github.com/Theara-Seng/stm32_lab/blob/main/input_capture/image/timer_runs_faster.png)

So we need to use another formula by set $ Capture = (TIMx_{period} - CNT0)+ CNT1 $ for case CNT0 > CNT1

## Configuration 
we need to configure the clock first 

![stm32F407VGT6](https://github.com/Theara-Seng/stm32_lab/blob/main/input_capture/image/clock.png)

After that, we can go into stm32 and this case I generate a pwm signal with frequency of 10KHz using Timer 1 as shown in here 


![stm32F407VGT6](https://github.com/Theara-Seng/stm32_lab/blob/main/input_capture/image/timer1.png)


Next, we need to configure the Timer 2 with input capture mode as shown in here 


![stm32F407VGT6](https://github.com/Theara-Seng/stm32_lab/blob/main/input_capture/image/timer2.png)

We also use interrupt in this timer 2


![stm32F407VGT6](https://github.com/Theara-Seng/stm32_lab/blob/main/input_capture/image/nvic.png)


# Programming 

First we create a pwm signal with the duty cycle of 30% and frequency of 10KHz 

```sh
 TIM1->CCR1 = 30;
 HAL_TIM_PWM_Start(&htim1, TIM_CHANNEL_1);
 ```
 
 After that we call the timer2 input caputure interrupt peripheral
 ```sh
 HAL_StatusTypeDef HAL_TIM_IC_Start_IT(TIM_HandleTypeDef *htim, uint32_t Channel)
 ```
 
 which is 
 
 ```sh
 HAL_TIM_IC_Start_IT(&htim2, TIM_CHANNEL_1);
 ```
 
 After that in the call back function
 
 ```sh
 
 uint32_t cap0 = 0;
uint32_t cap1 = 0;
uint32_t diff = 0;
uint8_t is_capture = 0;

/* Measure Frequency */
float frequency = 0;

void HAL_TIM_IC_CaptureCallback(TIM_HandleTypeDef *htim)
{
	if (htim->Channel == HAL_TIM_ACTIVE_CHANNEL_1)
	{
		if (is_capture==0)
		{
			cap0 = HAL_TIM_ReadCapturedValue(htim, TIM_CHANNEL_1);
			is_capture = 1;
		}

		else
		{
			cap1 = HAL_TIM_ReadCapturedValue(htim, TIM_CHANNEL_1);

			if (cap1 > cap0)
			{
				diff = cap1-cap0;
			}

			else if (cap0 > cap1)
			{
				diff = (0xffffffff - cap0) + cap1;
			}

			frequency = HAL_RCC_GetPCLK2Freq()/(htim2.Instance->PSC + 1);

			frequency = frequency/diff;


			__HAL_TIM_SET_COUNTER(htim, 0);  // reset the counter
			is_capture = 0; // set it back to false
		}
	}
}
```
After that in the while loop we can print the frequency capture 

```sh
	  printf("The frequency is %.2f\n", frequency);
	  HAL_Delay(1000);
 ```

# Result 
The graph below show the graph of the PWM signal with 30% duty cycle and frequency of 10KHz

![stm32F407VGT6](https://github.com/Theara-Seng/stm32_lab/blob/main/input_capture/image/duty.png)

Then the use USART 2 to transmit data to view the frequency 

![stm32F407VGT6](https://github.com/Theara-Seng/stm32_lab/blob/main/input_capture/image/frequency.png)
