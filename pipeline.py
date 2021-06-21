import apache-beam as beam

if __name__ == '__main__';
  
  with beam.Pipeline(argv=sys.argv) as p: //create a pipeline parameterized by command line flags
    
    (p
        | beam.io.ReadFromText('gs://<my-bucket>')  //Read inputs
        | beam.FlatMap(lambda line: count_words(line))  //Apply transform
        | beam.io.WriteToText('gs://<my-bucket>')
    )
    
  # end of with-clause: runs, stops the pipeline
  
  ** still WIP .. 
