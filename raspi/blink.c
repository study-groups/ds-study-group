int pin = 11;
int lightTime = 1000;
int dimTime = 200;

using GpioController controller = new();
controller.OpenPin(pin, PinMode.Output);

while (true)
{
    controller.Write(pin, PinValue.High);
    Thread.Sleep(lightTime);
    controller.Write(pin, PinValue.Low);
    Thread.Sleep(dimTime);
}
