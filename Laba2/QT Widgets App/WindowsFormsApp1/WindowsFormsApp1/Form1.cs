using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApp1
{
    public partial class Form1 : Form
    {
        private double a, b, h;
        private double x, y;
        public Form1()
        {
            InitializeComponent();
        }
         
        private void groupBox1_Enter(object sender, EventArgs e)
        {

        }

        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void построитьГрафикToolStripMenuItem_Click(object sender, EventArgs e)
        {
            if(checkBox_cos.Checked == false && checkBox_sin.Checked == false && checkBox_xsqr.Checked == false && checkBox_log.Checked == false && checkBox_xlog.Checked == false)
            {
                MessageBox.Show("Выберите хотя бы один график.", "Внимание!");
                return;
            }

            if(textBox_a.Text == "" || textBox_b.Text == "" || textBox_h.Text == "")
            {
                MessageBox.Show("Параметры по умолчанию.", "Внимание!");
                DefaultParams();
            }
            else
            {
                a = Convert.ToDouble(textBox_a.Text);
                b = Convert.ToDouble(textBox_b.Text);
                h = Convert.ToDouble(textBox_h.Text);
            }

            

            if(checkBox_cos.Checked)
            {
                x = a;
                this.chart.Series[0].Points.Clear();
                while (x <= b)
                {
                    y = Math.Cos(x);
                    this.chart.Series[0].Points.AddXY(x, y);
                    x += h;
                }
            }
            if (checkBox_sin.Checked)
            {
                x = a;
                this.chart.Series[1].Points.Clear();
                while (x <= b)
                {
                    y = Math.Sin(x);
                    this.chart.Series[1].Points.AddXY(x, y);
                    x += h;
                }
            }
            if (checkBox_xsqr.Checked)
            {
                x = a;
                this.chart.Series[2].Points.Clear();
                while (x <= b)
                {
                    y = x * x;
                    this.chart.Series[2].Points.AddXY(x, y);
                    x += h;
                }
            }
            if (checkBox_log.Checked)
            {
                if (textBox_a.Text == "" || textBox_b.Text == "" || textBox_h.Text == "")
                {
                    DefaultParamsForLog();
                }

                x = a;
                this.chart.Series[3].Points.Clear();
                while (x <= b)
                {
                    y = Math.Log(x);
                    this.chart.Series[3].Points.AddXY(x, y);
                    x += h;
                }
                DefaultParams();
            }
            if (checkBox_xlog.Checked)
            {
                if (textBox_a.Text == "" || textBox_b.Text == "" || textBox_h.Text == "")
                {
                    DefaultParamsForLog();
                }

                x = a;
                this.chart.Series[4].Points.Clear();
                while (x <= b)
                {
                    y = Math.Log(x) * x;
                    this.chart.Series[4].Points.AddXY(x, y);
                    x += h;
                }
                DefaultParams();
            }

        }

        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {

        }

        private void checkBox1_CheckedChanged_1(object sender, EventArgs e)
        {

        }

        private void checkBox_log_CheckedChanged(object sender, EventArgs e)
        {

        }

        private void очиститьГрафикToolStripMenuItem_Click(object sender, EventArgs e)
        {
            if (checkBox_cos.Checked == false && checkBox_sin.Checked == false && checkBox_xsqr.Checked == false && checkBox_log.Checked == false && checkBox_xlog.Checked == false)
            {
                MessageBox.Show("Выберите хотя бы один график.", "Внимание!");
                return;
            }

            if (checkBox_cos.Checked)
            {
                this.chart.Series[0].Points.Clear();
            }
            if (checkBox_sin.Checked)
            {
                this.chart.Series[1].Points.Clear();
            }
            if (checkBox_xsqr.Checked)
            {
                this.chart.Series[2].Points.Clear();
            }
            if (checkBox_log.Checked)
            {
                this.chart.Series[3].Points.Clear();
            }
            if (checkBox_xlog.Checked)
            {
                this.chart.Series[4].Points.Clear();
            }
        }

        private void label4_Click(object sender, EventArgs e)
        {

        }

        private void выходToolStripMenuItem_Click(object sender, EventArgs e)
        {
            if(MessageBox.Show("Выйти?","Внимание!",MessageBoxButtons.YesNo) == DialogResult.Yes)
            {
                Application.Exit();
            }
        }

        private void DefaultParams()
        {
            a = 0;
            b = 30;
            h = 0.1;
        }

        private void DefaultParamsForLog()
        {
            a = 1;
            b = 30;
            h = 0.1;
        }
    }
}
