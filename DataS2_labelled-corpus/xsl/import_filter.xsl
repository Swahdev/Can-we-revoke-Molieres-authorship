<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:tei= "http://www.tei-c.org/ns/1.0"
    xmlns:txm="http://textometrie.org/1.0"
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
    
    <!-- Remove punctuation -->
    <xsl:template match="tei:w[matches(txm:ana[@type='#frpos'], 'PON') or txm:form = ('«', '»')]"/>
        
    <!-- Remove preexisting ids -->    
    <xsl:template match="@id"/>
    
    <!-- Lower-case -->
    <xsl:template match="text()[parent::txm:form]">
        <xsl:value-of 
            select="normalize-unicode(lower-case(.), 'nfc')"/>
    </xsl:template>

</xsl:stylesheet>