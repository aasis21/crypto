

def encode(text ,block_size):
    text_length = len(text)
    amount_to_pad = block_size - (text_length % block_size)
    if amount_to_pad == 0:
        amount_to_pad = block_size
    pad = amount_to_pad
    if type(text)==bytes:
        return text + bytes([pad] * amount_to_pad)

    return text.encode() + bytes([pad] * amount_to_pad)


def decode(text):
    pad = text[-1]
    return text[:-pad]
