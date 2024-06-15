import java.awt.*;
import java.awt.event.*;
import java.applet.Applet;

public class Mouse extends Applet implements MouseListener {
    Label l;

    public Mouse() {
        l = new Label();
        l.setBounds(25, 60, 250, 30);
        l.setAlignment(Label.CENTER);
        this.add(l);
        this.setSize(300, 300);
        this.setLayout(null);
        this.setVisible(true);
        this.addMouseListener(this);
    }

    public static void main(String[] args) {
        new Mouse();
    }

    @Override
    public void mouseClicked(MouseEvent e) {
        l.setText("Mouse Clicked");
        repaint();
    }

    @Override
    public void mousePressed(MouseEvent e) {
        l.setText("Mouse Pressed");
        repaint();
    }

    @Override
    public void mouseReleased(MouseEvent e) {
        l.setText("Mouse Exited");
        repaint();
    }

    @Override
    public void mouseEntered(MouseEvent e) {
        setBackground(Color.RED);
    }

    @Override
    public void mouseExited(MouseEvent e) {
        setBackground(Color.WHITE);
    }
}