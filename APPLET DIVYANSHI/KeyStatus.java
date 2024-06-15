import java.applet.Applet;
import java.awt.Graphics;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

public class KeyStatus extends Applet implements KeyListener {
    String status = "";

    public void init() {
        setSize(400, 200);
        addKeyListener(this);
    }

    public void keyPressed(KeyEvent e) {
        status = "KeyPressed";
        repaint();
    }

    public void keyReleased(KeyEvent e) {
        status = "KeyReleased";
        repaint();
    }

    public void keyTyped(KeyEvent e) {
        status = "KeyTyped";
        repaint();
    }

    public void KeyUP(KeyEvent e) {
        status = "KeyUP";
        repaint();
    }

    public void KeyDown(KeyEvent e) {
        status = "KeyDown";
        repaint();
    }

    public void paint(Graphics g) {
        g.drawString("Status of key on an Applet window:", 10, 100);
        g.drawString(status, 10, 120);
    }
}