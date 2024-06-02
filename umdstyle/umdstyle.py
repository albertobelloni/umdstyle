#############################################
# UMD Style, based on a style file from BaBar
#############################################

import ROOT

umdStyle = None

def setUMDStyle():

    print ("\nApplying UMD style settings...\n")

    global umdStyle
    if umdStyle != None:
        del umdStyle

    umdStyle = ROOT.TStyle("umdStyle", "UMD Style")
    ROOT.gROOT.SetStyle(umdStyle.GetName())
    ROOT.gROOT.ForceStyle()

    # use plain black on white colors
    icol=ROOT.kWhite # WHITE
    umdStyle.SetFrameBorderMode(icol)
    umdStyle.SetFrameFillColor(icol)
    umdStyle.SetCanvasBorderMode(icol)
    umdStyle.SetCanvasColor(icol)
    umdStyle.SetPadBorderMode(icol)
    umdStyle.SetPadColor(icol)
    umdStyle.SetStatColor(icol)
    
    # set the paper & margin sizes
    umdStyle.SetPaperSize(20,26)
    
    # set margin sizes
    umdStyle.SetPadTopMargin(0.05)
    umdStyle.SetPadRightMargin(0.05)
    umdStyle.SetPadBottomMargin(0.16)
    umdStyle.SetPadLeftMargin(0.16)
    
    # set title offsets (for axis label)
    umdStyle.SetTitleXOffset(1.4)
    umdStyle.SetTitleYOffset(1.4)
    
    # set legend border size
    umdStyle.SetLegendBorderSize(0)
    
    # use large fonts
    #Int_t font=72 # Helvetica italics
    #Int_t font=42 # Helvetica:Arial
    font=82 # Courier New
    tsize=0.05
    umdStyle.SetTextFont(font)
    
    umdStyle.SetLegendFont(font)
    #umdStyle.SetLegendTextSize(tsize)
    
    umdStyle.SetTextSize(tsize)
    umdStyle.SetLabelFont(font,"XYZ")
    umdStyle.SetTitleFont(font,"XYZ")

    umdStyle.SetLabelSize(tsize,"XYZ")
    umdStyle.SetTitleSize(tsize,"XYZ")
    
    # use bold lines and markers
    umdStyle.SetMarkerStyle(20)
    umdStyle.SetMarkerSize(1.2)
    umdStyle.SetHistLineWidth(2)
    umdStyle.SetLineStyleString(2,"[12 12]") # postscript dashes
    
    # get rid of X error bars 
    #umdStyle.SetErrorX(0.001)
    # get rid of error bar caps
    umdStyle.SetEndErrorSize(0.)
    
    # do not display any of the standard histogram decorations
    umdStyle.SetOptTitle(0)
    umdStyle.SetOptStat(0)
    umdStyle.SetOptFit(0)

    #umdStyle.SetNdivisions(510, "XYZ")

    # put tick marks on top and RHS of plots
    umdStyle.SetPadTickX(1)
    umdStyle.SetPadTickY(1)
    
    umdStyle.cd()



