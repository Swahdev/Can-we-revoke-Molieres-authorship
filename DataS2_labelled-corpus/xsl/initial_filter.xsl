<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns=""
    xpath-default-namespace=""
    exclude-result-prefixes="xs"
    version="2.0">
   
    <!-- xml output -->
    <xsl:output method="xml" encoding="utf-8" omit-xml-declaration="yes"/>
    
    <!-- Default rule: identical copy -->
    <xsl:template match="@*|node()">
        <xsl:copy>
            <xsl:apply-templates select="@*|node()" />
        </xsl:copy>
    </xsl:template>
    
    <!-- Only text is kept inside TEI-->
    <xsl:template match="teiHeader | bottom"/>
    <xsl:template match="text">
        <xsl:copy>
        <xsl:apply-templates select="body"/>
        </xsl:copy>
    </xsl:template>
    
    <!-- All those elements are removed -->
    <xsl:template match="head|lg|note|p|poem|rhyme|s|speaker|stage"/>
    <!-- And all those divs are removed too -->
    <xsl:template match="div1[not(@type=('act', 'acte', 'scene', 'prologue'))]
        | div2[not(@type=('act', 'acte', 'scene', 'prologue'))]
        "/>
    
    <!-- Lower-case and remove punctuation
    Do not keep any text outside lines.
     -->
    <xsl:template match="text()[ancestor::l]">
        <xsl:value-of 
            select="normalize-unicode(lower-case(replace(., '\p{P}', ' ')), 'nfc')"/>
    </xsl:template>
    <xsl:template match="text()[not(ancestor::l)]"/>
    
</xsl:stylesheet>
