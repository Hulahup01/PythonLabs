from src.encoder.encoder import Encoder, Decoder

class A:
    a = 1

    @property
    def get_a(self):
        return self.a


if __name__ == '__main__':
    func = lambda val: val * val
    print(func(2))
    ser = Encoder.encode(func)
    des = Decoder.decode(ser)
    print(des(2))