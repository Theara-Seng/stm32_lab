# Input Capture Mode (Timer)

We use input capture to measure the frequency of a device which is generated from the device.

The **Input Capture Mode** offered by general purpose and advanced timers allows to compute the frequency of external singals applied to each one of the 4 channels that these timers provide. 
And the capture is perfored indepdently for each channel.


![stm32F407VGT6](https://github.com/Theara-Seng/stm32_lab/blob/main/input_capture/image/capture_process.png)


The image above shows how the caputure process works. **TIMx** is a timer, configured to workd given **TIMx_CLK** clock frequency. This means that it increment the **TIMx_CNT** register up to the 
period value every $\dfrac{1}{TIMx_CLK} second. 

Suppose that we apply a square wave signal to one of the timer channls, and supposing that we configure the timer to trigger at every rising edge of the input signal, we have that the **TIMx_CCRx**
