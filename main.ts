namespace SpriteKind {
    export const teleporter = SpriteKind.create()
}
sprites.onCreated(SpriteKind.Enemy, function (sprite) {
    sprite.follow(mySprite)
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    projectile = sprites.createProjectileFromSprite(assets.image`Throw you a bone`, mySprite, 50, 0)
    animation.runImageAnimation(
    projectile,
    [img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `],
    100,
    true
    )
})
sprites.onOverlap(SpriteKind.Enemy, SpriteKind.Player, function (sprite2, otherSprite) {
    info.changeLifeBy(-1)
    music.jumpDown.play()
    sprite2.destroy()
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite3, otherSprite2) {
    otherSprite2.destroy()
})
info.onLifeZero(function () {
    game.over(false)
    tiles.loadMap(tiles.createMap(tilemap`level2`))
})
let enemy_sprite: Sprite = null
let projectile: Sprite = null
let mySprite: Sprite = null
class ActionKind {
    static Walking = 0
    static Idle = 1
    static Jumping = 2
}
mySprite = sprites.create(assets.image`Skeleton`, SpriteKind.Player)
mySprite.setVelocity(60, 60)
tiles.setTilemap(tilemap`The map`)
scene.cameraFollowSprite(mySprite)
scene.setBackgroundImage(assets.image`the graves`)
game.splash("You've risen, I haven't seen you in quite some time, You've grown! anyway, they`re trying to kill you, but this time they'll kill you dead, RUN ")
info.setLife(2)
controller.moveSprite(mySprite)
animation.setAction(mySprite, ActionKind.Walking)
tiles.createSpritesOnTiles(assets.tile`myTile13`, SpriteKind.Player)
game.onUpdateInterval(5000, function () {
    enemy_sprite = sprites.create(img`
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
        `, SpriteKind.Enemy)
    enemy_sprite.setPosition(randint(0, scene.screenWidth()), randint(0, scene.screenHeight()))
    enemy_sprite.setVelocity(1, 1)
})
forever(function () {
    music.playMelody("C D E D F D E D ", 128)
})
