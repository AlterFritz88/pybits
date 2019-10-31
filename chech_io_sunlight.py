def sun_angle(time):
    hour, minute = int(time.split(':')[0]), int(time.split(':')[1])
    if hour < 6 or (hour >= 18 and minute != 0):
        return "I don't see the sun!"
    hour -= 6
    ans = hour * 15 + minute * 0.25
    return ans

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")