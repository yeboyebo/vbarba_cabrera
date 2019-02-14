class client {
    siguienteCarro(){
        var numCarro = parseInt(YEBOYEBO.$("#labelNumCarro").text()) + 1;
        if(numCarro >= 1)
            YEBOYEBO.$("#labelNumCarro").html(numCarro);
        else numCarro = 1;
        return numCarro;
    }

    anteriorCarro(){
        var numCarro = parseInt(YEBOYEBO.$("#labelNumCarro").text()) - 1;
        if(numCarro >= 1)
            YEBOYEBO.$("#labelNumCarro").html(numCarro);
        else numCarro = 1;
        return numCarro;
    }

    siguientePiso(){
        var numPiso = parseInt(YEBOYEBO.$("#labelNumPiso").text()) + 1;
        if(numPiso >= 1)
            YEBOYEBO.$("#labelNumPiso").html(numPiso);
        else numPiso = 1;
        return numPiso;
    }

    anteriorPiso(){
        var numPiso = parseInt(YEBOYEBO.$("#labelNumPiso").text()) - 1;
        if(numPiso >= 1)
            YEBOYEBO.$("#labelNumPiso").html(numPiso);
        else numPiso = 1;
        return numPiso;
    }
}