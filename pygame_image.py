import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex01/fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_img_r = pg.transform.rotozoom(kk_img, 10, 1.0)
    # kk_imgとkk_img_rを要素とするリストを作成
    kk_imgs = [kk_img, kk_img_r]

    
    tmr = 0
    bg_x = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [-bg_x, 0])
        screen.blit(bg_img, [1600-bg_x, 0])
        # 横300,縦200の位置にkk_imgsを描画　交互に表示
        screen.blit(kk_imgs[tmr%2], [300, 200])
        pg.display.update()
        tmr += 1        
        clock.tick(100)
        bg_x += 1
        if bg_x >= 1600: bg_x = 0


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()