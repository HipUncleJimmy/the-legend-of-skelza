class ActionKind(Enum):
    Walking = 0
    Idle = 1
    Jumping = 2

def on_on_created(sprite):
    sprite.follow(mySprite)
sprites.on_created(SpriteKind.enemy, on_on_created)

def on_a_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(assets.image("""
        Throw you a bone
    """), mySprite, 50, 0)
    animation.run_image_animation(projectile,
        [img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . d 1 1 . . 1 1 1 . . . . 
                        . . . . d d d 1 1 1 d d . . . . 
                        . . . . . . d 1 1 1 . . . . . . 
                        . . . . . . d 1 1 1 . . . . . . 
                        . . . . d 1 1 1 1 1 1 1 . . . . 
                        . . . . d d . . . . d d . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . 1 . . . 1 1 . . 
                        . . . d 1 1 . 1 1 . . 1 1 . . . 
                        . . . d 1 1 1 1 . . 1 1 . . . . 
                        . . . d 1 1 1 . . . 1 . . . . . 
                        . . . d d d 1 1 . 1 . . . . . . 
                        . . . . . d d 1 1 . 1 1 . . . . 
                        . . . . . . d d 1 1 1 . 1 . . . 
                        . . . . . . . d d 1 . 1 1 . . . 
                        . . . . . . . . d d d 1 1 . . . 
                        . . . . . . . . . . d 1 1 . . . 
                        . . . . . . . . . . d 1 1 . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . 1 . . . . 
                        . . . . . . . d d d . 1 . . . . 
                        . . . . . . . d 1 1 1 1 . . . . 
                        . . . . . . . d 1 1 1 . 1 1 . . 
                        . . . . . . . . d . . . 1 . . . 
                        . . . . . . . . d 1 1 1 . . . . 
                        . . . . . . . . d 1 . . . . . . 
                        . . . . . . . d 1 1 . 1 . . . . 
                        . . . . . . . d 1 1 1 1 . . . . 
                        . . . . . . . d 1 1 . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . 1 1 1 . . . . 
                        . . . . . . . . . 1 1 1 . . . . 
                        . . . . . . . . 1 1 1 1 . . . . 
                        . . . . . . . 1 1 . 1 1 . . . . 
                        . . . . . 1 1 1 1 . . . . . . . 
                        . . . . . 1 1 1 1 1 . . . . . . 
                        . . . . . 1 1 1 . 1 1 1 . . . . 
                        . . . . . . 1 1 . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """)],
        100,
        True)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite2, otherSprite):
    info.change_life_by(-1)
    music.jump_down.play()
    sprite2.destroy()
sprites.on_overlap(SpriteKind.enemy, SpriteKind.player, on_on_overlap)

def on_life_zero():
    game.over(False)
info.on_life_zero(on_life_zero)

def on_on_overlap2(sprite3, otherSprite2):
    otherSprite2.destroy()
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap2)

enemy_sprite: Sprite = None
projectile: Sprite = None
mySprite: Sprite = None
mySprite = sprites.create(assets.image("""
    Skeleton
"""), SpriteKind.player)
scene.camera_follow_sprite(mySprite)
scene.set_background_image(assets.image("""
    the graves
"""))
game.splash("You've risen, I haven't seen you in quite some time, You've grown! anyway, they`re trying to kill you, but this time they'll kill you dead, RUN ")
tiles.set_tilemap(tilemap("""
    level1
"""))
info.set_life(5)
controller.move_sprite(mySprite)
animation.set_action(mySprite, ActionKind.Walking)

def on_forever():
    music.play_melody("C D E D F D E D ", 128)
forever(on_forever)

def on_update_interval():
    global enemy_sprite
    enemy_sprite = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . d d 1 1 1 1 1 1 1 . . . . 
                    . . d d 1 1 1 1 1 1 1 1 1 . . . 
                    . . d 1 1 1 1 1 1 1 1 1 1 1 . . 
                    . . d 1 1 f 1 1 1 1 1 f 1 1 . . 
                    . . d 1 1 f 1 1 1 1 1 f 1 1 . . 
                    . . d 1 1 f 1 1 1 1 1 f 1 1 . . 
                    . . d 1 1 1 1 1 1 1 1 1 1 1 . . 
                    . . d 1 1 1 1 1 1 1 1 1 1 1 . . 
                    . . d 1 1 1 1 1 1 1 1 1 1 1 . . 
                    . . d 1 1 1 1 1 1 1 1 1 1 1 . . 
                    . . d 1 1 1 1 1 1 1 1 1 1 1 . . 
                    . . d 1 d 1 d 1 d 1 d 1 d 1 . . 
                    . . . d . d . d . d . d . d . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.enemy)
    enemy_sprite.set_position(randint(0, scene.screen_width()),
        randint(0, scene.screen_height()))
game.on_update_interval(10000, on_update_interval)
