import pygame
import sys
# Configuration de la fenêtre
LARGEUR, HAUTEUR = 1280, 800
ecran = pygame.display.set_mode((LARGEUR, HAUTEUR), pygame.FULLSCREEN)
pygame.display.set_caption("Basket ball 2D ninja ")


joueur_image = pygame.image.load("./img/ninja.png")  # Remplacez par 
joueur_rect = joueur_image.get_rect(center=(LARGEUR//2, HAUTEUR//2))


vitesse = 15

clock = pygame.time.Clock()

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    touches = pygame.key.get_pressed()
    if touches[pygame.K_LEFT]:
        joueur_rect.x -= vitesse
    if touches[pygame.K_RIGHT]:
        joueur_rect.x += vitesse
    if touches[pygame.K_UP]:
        joueur_rect.y -= vitesse
    if touches[pygame.K_DOWN]:
        joueur_rect.y += vitesse

    # 3. Limites de l'écran (Optionnel mais recommandé)
    joueur_rect.clamp_ip(ecran.get_rect()) #value = ecran.get_rect()

    # 4. Rendu
#    ecran.fill((30, 30, 30))  # Effacer l'écran avec une couleur de fond
    bg = pygame.image.load("./img/bg-plage_night.png").convert()
    bg = pygame.transform.smoothscale(bg, ecran.get_size())
    for x in range(0, LARGEUR, bg.get_width()):
        for y in range (0, HAUTEUR, bg.get_height()):
        	ecran.blit(bg,(x,y))
        	
    ecran.blit(joueur_image, joueur_rect)
    
    pygame.display.flip()  # Mettre à jour l'affichage
    clock.tick(60)         # Limiter à 60 FPS

pygame.quit()
sys.exit()
