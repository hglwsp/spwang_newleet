from Crypto.Cipher import DES
import os
import random
import string

def pad(data):
    # DES块大小为8字节，填充数据以使其长度为8的倍数
    padding_length = 8 - (len(data) % 8)
    padding = chr(padding_length) * padding_length
    return data + padding

def unpad(data):
    # 去除填充
    padding_length = ord(data[-1])
    return data[:-padding_length]

def generate_key():
    # 生成一个8字节的密钥
    return os.urandom(8)

def encrypt(data, key):
    # 创建DES加密对象
    cipher = DES.new(key, DES.MODE_ECB)
    # 加密数据
    encrypted_data = cipher.encrypt(pad(data).encode())
    return encrypted_data

def decrypt(encrypted_data, key):
    # 创建DES解密对象
    cipher = DES.new(key, DES.MODE_ECB)
    # 解密数据
    decrypted_data = cipher.decrypt(encrypted_data)
    return unpad(decrypted_data.decode())

def generate_random_string(length):
    # 生成随机字符串
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))


def main():
    # 生成密钥
    key = generate_key()

    # 测试100组随机用户名和密码
    flag = 1
    for _ in range(100):
        username = generate_random_string(random.randint(5, 15))
        password = generate_random_string(random.randint(5, 15))

        # 加密用户名和密码
        encrypted_username = encrypt(username, key)
        encrypted_password = encrypt(password, key)

        # 解密用户名和密码
        decrypted_username = decrypt(encrypted_username, key)
        decrypted_password = decrypt(encrypted_password, key)

        # 打印原始值、加密值、解密值
        print(f"第{flag}组")
        print(f"原始用户名: {username}")
        print(f"加密后的用户名: {encrypted_username.hex()}")
        print(f"解密后的用户名: {decrypted_username}")

        print(f"原始密码: {password}")
        print(f"加密后的密码: {encrypted_password.hex()}")
        print(f"解密后的密码: {decrypted_password}")
        print("-" * 40)
        flag+=1

if __name__ == "__main__":
    main()