# Import the TV class from the TV module
from tv import TV


# Define a function to test the TV class
def test_tv():

    # Create a TV object tv1
    tv1 = TV(channel=30, volume=3, is_on=True)
    # Create a TV object tv2
    tv2 = TV(channel=3, volume=2, is_on=True)

    # Print the channel and volume level of tv1
    print("\033[92mTv 1's channel is ", {tv1.get_channel()}, " and volume level is ", {tv1.get_volume()}, "\033[0m")
    # Print the channel and volume level of tv2
    print("\033[92mTv 2's channel is ", {tv2.get_channel()}, " and volume level is ", {tv2.get_volume()}, "\033[0m")


# Run the tests if this script is executed directly
intro = ' Test Tv Program'.center(50, '-')
print(f"\033[94m {intro} \033[0m")
print()

test_tv()

print()
outro = " Test Ended ".center(50, '-')
print(f"\033[94m {outro} \033[0m")
