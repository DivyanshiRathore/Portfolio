import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Marks extends JFrame {
    private JTextField[] subjectFields;
    private JLabel resultLabel;

    public Marks()
    {
        setTitle("Students Marks Entry");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new GridLayout(0,2));

        subjectFields = new JTextField[5];
        for(int i=0;i<5;i++)
        {
            subjectFields[i]=new JTextField(10);
            add(new JLabel("subject"+(i+1)+":"));
            add(subjectFields[i]);
        }
        JButton submitButton=new JButton("Submit");
        submitButton.addActionListener(new ActionListener()
        {
            @Override
            public void actionPerformed(ActionEvent e){
                int totalMarks=0;
                for(JTextField field:subjectFields)
                {
                    try{
                        totalMarks+=Integer.parseInt(field.getText());
                    }
                    catch(NumberFormatException ex)
                    {
                        JOptionPane.showMessageDialog(null,"Please enter valid marks for all subjects","Invalid Marks",JOptionPane.ERROR_MESSAGE);
                        return;
                    }
                }
                double averageMarks=(double) totalMarks/subjectFields.length;
                ResultWindow resultWindow=new ResultWindow(averageMarks);
                resultWindow.setVisible(true);
            }
        });
        add(submitButton);
        pack();
        setLocationRelativeTo(null);
        }

    private class ResultWindow extends JDialog {
        public ResultWindow(double averageMarks) {
            setTitle("Students Result");

            setDefaultCloseOperation(JDialog.DISPOSE_ON_CLOSE);
            setLayout(new GridLayout(0, 1));

            resultLabel = new JLabel();
            resultLabel.setHorizontalAlignment(JLabel.CENTER);
            if (averageMarks >= 60) {
                resultLabel.setText("congratulations! your average marks is" + averageMarks + ".you have passed.");
                resultLabel.setForeground(Color.BLUE);
            } else {
                resultLabel.setText("SORRY! your average marks is" + averageMarks + ".You have Failed.");
                resultLabel.setForeground(Color.RED);
            }
            add(resultLabel);
            pack();
        }
    }

    public static void main(String[] args) {
        new Marks().setVisible(true);
    }
}
