# 3D Games

The author has created a library similar to Pygame Zero but for creating 3d games: *richlib*. It is still experimental and subject to change.  The newest
version at time of writng is 0.0.6.

If you are using Mu then add the package ```richlib==0.0.6```

If you are using IDLE then type at the command line:

```pip3 install richlib==0.0.6```

Richlib is similar to Pygame Zero, but there are some differences.

You now have to put

```run()```

at the end of your programs.

This calls a method in Richlib. You can’t see it, but what it does is something like this:

```python
def run():
    while True:
        update()
        draw()
        time.sleep(0.1)
```