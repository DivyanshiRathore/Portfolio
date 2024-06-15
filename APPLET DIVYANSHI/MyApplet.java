import java.applet.Applet;
import java.awt.Graphics;

public class MyApplet extends Applet {
    String s = null;

    public void init() {
        s = getParameter("msg");
    }

    public void paint(Graphics g) {
        g.drawString(s, 50, 50);
    }
}