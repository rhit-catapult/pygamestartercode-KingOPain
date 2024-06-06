import pygame
import sys


def main():
    # pre-define RGB colors for Pygame
    BLACK = pygame.Color("Black")
    WHITE = pygame.Color("White")
    IMAGE_SIZE = 470
    TEXT_HEIGHT = 30

    # initialize the pygame module
    pygame.init()

    # prepare the window (screen)
    screen = pygame.display.set_mode((IMAGE_SIZE, IMAGE_SIZE + TEXT_HEIGHT))
    pygame.display.set_caption("Text, Sound, and an Image")

    # Prepare the image
    # DONE 1: Create an image with the 2dogs.JPG image
    image = pygame.image.load("2dogs.JPG")
    # DONE 3: Scale the image to be the size (IMAGE_SIZE, IMAGE_SIZE)
    image = pygame.transform.scale(image, (IMAGE_SIZE, IMAGE_SIZE))

    # Prepare the text caption(s)
    # DONE 4: Create a font object with a size 28 font.
    font1 = pygame.font.SysFont("papyrus", 28)
    # DONE 5: Render the text "Two Dogs" using the font object (it's like MAKING an image).
    caption1 = font1.render("Two Dogs", True, (158, 45, 99))

    font2 = pygame.font.SysFont("papyrus", 50)
    caption2 = font2.render("Foo", True, (22, 165, 149))


    # Prepare the music
    # DONE 8: Create a Sound object from the "bark.wav" file.
    bark = pygame.mixer.Sound("bark.wav")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # DONE 9: Play the music (bark) if there's a mouse click.
            if event.type == pygame.MOUSEBUTTONDOWN:
                bark.play()

        # Clear the screen and set the screen background
        screen.fill(WHITE)

        # Draw the image onto the screen
        # DONE 2: Draw (blit) the image onto the screen at position (0, 0)
        screen.blit(image, (0,0))

        # Draw the text onto the screen
        # DONE 6: Draw (blit) the text image onto the screen in the middle bottom.
        screen.blit(caption1, ((IMAGE_SIZE - caption1.get_width())/2, 463))
        # Hint: Commands like these might be useful..
        #          screen.get_width(), caption1.get_width(), image1.get_height()

        # DONE 7: On your own, create a new bigger font and in white text place a 'funny' message on top of the image.

        screen.blit(caption2, (122, 3))
        # Update the screen
        pygame.display.update()


main()
