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
